import re
import time

import pandas

from analyse.qps_cpu_painter import draw_qps_gc, draw_throughput_time_gc


# Return list of [time str, all qps, standalone operation qps ...]
def get_ops(path, operations):
    re_strs = []
    re_strs.append(("ALL", "[0-9]+ operations"))
    for op in operations:
        re_str = r"\[" + op + ": Count=[0-9]+"
        re_strs.append((op, re_str))

    result_list = []
    with open(path, encoding='utf-8') as file:
        pre_ops_map = {key: 0 for key in operations}
        for line in file:
            res = []
            time_str = line[:19]
            res.append(time_str)

            for re_str in re_strs:
                match_res = re.search(re_str[1], line)
                re_res = match_res.group()
                if re_str[0] == "ALL":
                    res.append(int(re_res[:-(len(" operations"))]))
                else:
                    ops = int(re_res[len("[" + re_str[0] + ": Count="):])
                    res.append(ops - pre_ops_map[re_str[0]])
                    pre_ops_map[re_str[0]] = ops
            result_list.append(res)
    return result_list


# Return list of [start timestamp, end timestamp, duration]
# Time accuracy: second
def get_gc(path):
    gc_time_data = pandas.read_csv(path)

    result = []
    for index, row in gc_time_data.iterrows():
        start_time = phrase_time(row['start time'])
        end_time = phrase_time(row['end time'])
        duration = end_time - start_time
        result.append((start_time, end_time, duration))

    return result


def gc_count_at_time(gc_list, time_list):
    result = []
    for time_point in time_list:
        count = 0
        for gc in gc_list:
            if gc[0] <= time_point < gc[1]:
                count += 1
        result.append(count)
    return result


# input example:'2023-05-10 10:49:35'
def phrase_time(time_str):
    # dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    if isinstance(time_str, str):
        time_array = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        timestamp = int(time.mktime(time_array))
        return timestamp
    else:
        return time_str//1000000


def main():
    qps_file = "/Users/fenghao/Desktop/offload/overall/ycsb-titan-120G/UPDATE"
    gc_file = "/Users/fenghao/Desktop/offload/overall/ycsb-titan-120G/GC_TIME"

    ops_res = get_ops(qps_file, ["READ", "UPDATE"])
    gc_time = get_gc(gc_file)

    x0 = phrase_time(ops_res[0][0])
    x = [phrase_time(ops[0]) - x0 for ops in ops_res]
    qps_res = [ops[1] // 10 for ops in ops_res]
    for i in range(len(qps_res) - 1, 0, -1):
        qps_res[i] -= qps_res[i - 1]
    gc_res = gc_count_at_time(gc_time, [phrase_time(ops[0]) for ops in ops_res])
    # draw_qps_gc(x, qps_res, gc_res)
    draw_throughput_time_gc(x, qps_res, gc_res)


if __name__ == '__main__':
    main()
