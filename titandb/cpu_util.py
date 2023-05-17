import sys
import time
import psutil


def main():
    # get pid from args
    if len(sys.argv) < 2:
        print("missing pid arg")
        sys.exit()

    # get process
    pid = int(sys.argv[1])
    p = psutil.Process(pid)

    interval = 1
    with open("CPU", "a+") as f:
        f.write("time,cpu%,mem%\n")  # titles
        while True:
            lines = []
            for _ in range(30):
                line = get_usage_line(p)
                lines.append(line)
                time.sleep(interval)
            f.write(''.join(lines))


def get_usage_line(p):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    cpu_percent = p.cpu_percent()
    mem_percent = p.memory_info().rss
    line = current_time + ',' + str(cpu_percent) + ',' + str(mem_percent) + "\n"
    return line


if __name__ == '__main__':
    main()
