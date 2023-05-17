from analyse.parameters_painter import draw_params
from analyse.qps import get_gc


def get_cpu_list(paths):
    cpu_paths = [path + "/CPU_UPDATE" for path in paths]
    pass


def get_gc_info_list(paths):
    gc_paths = [path + "/GC_TIME" for path in paths]
    result_list = []
    for gc_path in gc_paths:
        gc_time = get_gc(gc_path)
        result_list.append((len(gc_time), sum([t[2] for t in gc_time]) / len(gc_time)))
    return result_list


def main():
    params = ["0.5-512-1024MB", "0.5-64-256MB", "0.45-64-512MB", "0.40-64-512MB", "0.35-64-512MB", "0.25-64-512MB"]
    spaces = [42, 43, 41, 34, 29, 28]
    paths = ["/Users/fenghao/Desktop/ycsb_test/20M-80M-" + param + "-" + str(space) + "G" for param, space in
             zip(params, spaces)]
    throughput_list = [8215, 8443, 8146, 6435, 5444, 4419]  # qps
    io_list = [(7994, 20566), (7215, 18304), (11786, 25098), (22408, 44644), (31629, 60045),
               (52387, 81576)]  # (titandb.gc.bytes.written, titandb.gc.bytes.read) MB
    # todo cpu指标用什么方式衡量？
    # cpu_list = get_cpu_list(paths)
    gc_info_list = get_gc_info_list(paths)  # [(times, avg duration), ...]
    space_amp_list = [space / 20 for space in spaces]
    draw_params(params, throughput_list, space_amp_list, io_list, gc_info_list)


if __name__ == '__main__':
    main()
