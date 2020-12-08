import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def plot_cache(ax, real_file, sim_file, patterns, color_real="gainsboro", color_wrench="tab:cyan"):
    index = ["file_1", "file_2", "file_3", "file_4"]
    columns = ["Read 1", "Write 1", "Read 2", "Write 2", "Read 3", "Write 3"]

    df_real = pd.read_csv(real_file, index_col="task")
    df_sim = pd.read_csv(sim_file, index_col="task")

    df_real[index].plot.bar(stacked=True, rot=0, color=color_real, edgecolor="k", ax=ax, position=1, width=0.3, legend=False, linewidth=0.5)
    df_sim[index].plot.bar(stacked=True, rot=0, color=color_wrench, edgecolor="k", ax=ax, position=0, width=0.3, legend=False, linewidth=0.5)

    ax.set_xlabel("tasks")
    ax.set_ylabel("amount (GB)")
    ax.set_xticklabels(columns)

    bars = ax.patches
    hatches = []  # list for hatches in the order of the bars
    for h in patterns:  # loop over patterns to create bar-ordered hatches
        for i in range(len(columns)):
            hatches.append(h)
    for h in patterns:  # loop over patterns to create bar-ordered hatches
        for i in range(len(columns)):
            hatches.append(h)
    for bar, hatch in zip(bars, hatches):  # loop over bars and hatches to set hatches in correct order
        bar.set_hatch(hatch)

    ax.set_xlim(left=-0.5)
    ax.set_ylim(top=180)


def plot_cache_v2():

    files = ["file 1", "file 2", "file 3", "file 4"]
    envs = ["Real execution", "WRENCH-cache"]
    patterns = ["", "...", "///", "\\\\\\"]
    color_real = "gainsboro"
    color_wrench = "tab:cyan"

    fig, (ax1, ax2) = plt.subplots(figsize=(11, 4), ncols=2, nrows=1)
    plt.subplots_adjust(left=0.1, bottom=0.15, right=0.95, top=0.8, wspace=0.25)
    plt.rcParams.update({'font.size': 9})

    plot_cache(ax1, "fincore/real_20gb.csv", "fincore/sim_20gb.csv", patterns)
    plot_cache(ax2, "fincore/real_100gb.csv", "fincore/sim_100gb.csv", patterns)

    legend_elements = [Patch(facecolor=color_real),
                       Patch(facecolor=color_wrench),
                       Patch(facecolor='w', hatch="", edgecolor='k'),
                       Patch(facecolor='w', hatch="...", edgecolor='k'),
                       Patch(facecolor='w', hatch="///", edgecolor='k'),
                       Patch(facecolor='w', hatch="\\\\\\", edgecolor='k')]

    ax1.set_title("20 GB")
    ax2.set_title("100 GB")

    plt.legend(legend_elements, envs + files, ncol=3, loc='upper center', bbox_to_anchor=(-0.1, 1.3))
    plt.savefig("figures/cached_files.svg", format="svg")
    plt.savefig("figures/cached_files.pdf", format="pdf")

    # plt.show()
