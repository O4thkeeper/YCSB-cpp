import pandas

from analyse.qps_cpu_painter import draw_cpu_gc
from analyse.qps import phrase_time, get_gc, gc_count_at_time


def get_cpu_usage(path):
    cpu_usage_data = pandas.read_csv(path)

    result = []
    for index, row in cpu_usage_data.iterrows():
        timestamp = phrase_time(row['time'])
        cpu_usage = row['cpu%']
        result.append((timestamp, cpu_usage))

    return result


def main():
    cpu_file = "/Users/fenghao/Desktop/ycsb_test/20M-80M-0.25-64-512MB-28G/CPU_UPDATE"
    gc_file = "/Users/fenghao/Desktop/ycsb_test/20M-80M-0.25-64-512MB-28G/GC_TIME"

    cpu_usage = get_cpu_usage(cpu_file)

    x0 = cpu_usage[0][0]
    x = [cu[0] - x0 for cu in cpu_usage]

    cpu_res = [cu[1] for cu in cpu_usage]

    gc_time = get_gc(gc_file)
    gc_res = gc_count_at_time(gc_time, [cu[0] for cu in cpu_usage])

    draw_cpu_gc(x, cpu_res, gc_res)


if __name__ == '__main__':
    main()
