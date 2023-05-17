import matplotlib.pyplot as plt
import numpy as np


def init_plt_env():
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False


def qps_draw(ax, x_data, y_data):
    ax.scatter(x_data, y_data, c="b", s=1, label="Throughput")
    ax.set_xlabel("Elapsed Seconds", fontsize=12)
    ax.set_ylabel("Throughput (ops/sec)", fontsize=12)
    ax.tick_params("y", color="b")


def cpu_draw(ax, x_data, y_data):
    ax.scatter(x_data, y_data, c="b", s=1, label="CPU Usage")
    ax.set_xlabel("Elapsed Seconds", fontsize=12)
    ax.set_ylabel("CPU Usage (%)", fontsize=12)
    ax.tick_params("y", color="b")


def gc_draw(ax, x_data, y_data):
    ax.scatter(x_data, y_data, c="r", s=1, label="GC Count")
    ax.set_ylabel("GC Count (ops)", fontsize=12, rotation=-90, labelpad=12)
    ax.set_yticks(np.arange(0, max(y_data) + 3, 1))
    ax.tick_params("y", color="r")


def draw_qps_gc(x, qps_res, gc_res):
    init_plt_env()
    fig, ax1 = plt.subplots()
    qps_draw(ax1, x, qps_res)

    ax2 = ax1.twinx()
    gc_draw(ax2, x, gc_res)

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, markerscale=5, loc='best')

    plt.tight_layout()
    plt.show()


def draw_cpu_gc(x, qps_res, gc_res):
    init_plt_env()
    fig, ax1 = plt.subplots()
    cpu_draw(ax1, x, qps_res)

    ax2 = ax1.twinx()
    gc_draw(ax2, x, gc_res)

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, markerscale=5, loc='best')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    pass
