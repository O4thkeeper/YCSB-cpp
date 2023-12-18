import matplotlib.pyplot as plt
import numpy as np


def init_plt_env():
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False


def triple_bar_draw(ax, x_data, y1_data, y2_data, y3_data, labels, title, colors):
    x = np.arange(len(x_data))
    width = 0.3

    ax.bar(x - width, y1_data, width, label=labels[0], color=colors[0])
    # ax.set_ylabel('Throughput', fontsize=12)

    ax.bar(x, y2_data, width, label=labels[1], color=colors[1])
    ax.bar(x + width, y3_data, width, label=labels[2], color=colors[2])
    ax.legend()

    ax.set_title(title, fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(x_data)


def main():
    titles = ['YCSB 4KB', 'YCSB 1KB']
    x = ['load', 'A', 'B', 'C', 'D', 'E', 'F']
    labels = ['ALTree', 'MatrixKV', 'NoveLSM']
    colors = [(219 / 255, 49 / 255, 36 / 255), (252 / 255, 140 / 255, 90 / 255), (255 / 255, 223 / 255, 146 / 255),
              (78 / 255, 171 / 255, 144 / 255)]

    al_4 = [54583.82, 43430.94, 24099.88, 16467.6, 18888.45, 4686.2, 30793.99]
    ma_4 = [6886.72, 8504.06, 6239.13, 5552.97, 5716.8, 685.57, 6492.15]
    no_4 = [10789.34, 19254.66, 16592.27, 14392.06, 13486.64, 3284.46, 15126.48]

    al_1 = [90486.03, 47823.98, 27275.43, 18246.14, 13762.1, 6860.41, 22805.3]
    ma_1 = [23859.48, 277.24, 200.42, 3634.48, 3448.62, 715.24, 10492.45]
    no_1 = [26266.18, 1452.31, 865.28, 6933.54, 337.34, 402.43, 493.82]

    for a, m, n in zip(al_1, ma_1, no_1):
        print(a / m, a / n)

    # init_plt_env()
    # fig = plt.figure(figsize=(9, 4))
    # axs = fig.subplots(1, 2)
    #
    # triple_bar_draw(axs[0], x, al_4, ma_4, no_4, labels, titles[0], colors)
    # triple_bar_draw(axs[1], x, al_1, ma_1, no_1, labels, titles[1], colors)
    #
    # plt.tight_layout()
    # plt.show()
    # plt.savefig('/Users/fenghao/Desktop/ycsb.jpg', dpi=500)


if __name__ == '__main__':
    main()
