import matplotlib.pyplot as plt
import numpy as np


def init_plt_env():
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False


def bar_draw(ax, x_data, y_data, title, color, y_label):
    ax.bar(x_data, y_data, width=0.6, color=color)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(title, fontsize=16)


def double_bar_draw(ax, x_data, y1_data, y2_data, y1_label, y2_label, title, colors, same_y=False, y_label=None):
    x = np.arange(len(x_data))
    width = 0.35

    ax.bar(x - width / 2, y1_data, width, label=y1_label, color=colors[0])
    if y_label is None:
        ax.set_ylabel(y1_label, fontsize=12)
    else:
        ax.set_ylabel(y_label[0], fontsize=12)

    if same_y:
        ax.bar(x + width / 2, y2_data, width, label=y2_label, color=colors[1])
        ax.legend()
    else:
        ax2 = ax.twinx()
        ax2.bar(x + width / 2, y2_data, width, label=y2_label, color=colors[1])
        if y_label is None:
            ax2.set_ylabel(y2_label, fontsize=12, rotation=-90, labelpad=10)
        else:
            ax2.set_ylabel(y_label[1], fontsize=12, rotation=-90, labelpad=10)

        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2)

    ax.set_title(title, fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(x_data)


def draw_params(params, throughput_list, space_amp_list, io_list, gc_info_list):
    init_plt_env()
    fig = plt.figure(figsize=(12, 8))
    axs = fig.subplots(2, 2)

    x = [chr(ord('A') + i) for i in range(len(params))]
    bar_draw(axs[0, 0], x, throughput_list, "THROUGHPUT", (246 / 255, 111 / 255, 105 / 255),
             "Throughput (ops/sec)")

    bar_draw(axs[0][1], x, space_amp_list, "SPACE AMP", (254 / 255, 179 / 255, 174 / 255), "Space Amplification")

    colors = [(144 / 255, 201 / 255, 231 / 255), (33 / 255, 158 / 255, 188 / 255)]
    output_list = [io[0] for io in io_list]
    input_list = [io[1] for io in io_list]
    double_bar_draw(axs[1][0], x, input_list, output_list, "Read", "Write", "IO", colors, True, ["Data Size (MB)"])

    colors = [(102 / 255, 205 / 255, 170 / 255), (78 / 255, 171 / 255, 144 / 255)]
    gc_times_list = [gc_info[0] for gc_info in gc_info_list]
    gc_duration_list = [gc_info[1] for gc_info in gc_info_list]
    double_bar_draw(axs[1][1], x, gc_times_list, gc_duration_list, "GC Frequency", "Average Duration", "GC INFO",
                    colors, False, ["Frequency (ops)", "Duration (sec)"])

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    pass
