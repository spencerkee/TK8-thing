import os

plots_dir = "plots"
os.makedirs(plots_dir, exist_ok=True)

import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

from enums import dan_names_dict


def plot_win_rates(win_rates, bracket_name=""):
    # plot the win rates with confidence intervals
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(win_rates.keys()), y=list(win_rates.values()))
    plt.title(f"Win Rates_{bracket_name}")
    plt.xlabel("Character")
    plt.ylabel("Win Rate")
    plt.ylim(0.44, 0.6)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(
        os.path.join(
            plots_dir, f"win_rates_with_confidence_intervals_{bracket_name}.png"
        )
    )
    plt.show()


def plot_win_rates_with_confidence_intervals(
    win_rates, confidence_intervals, bracket_name=""
):
    # plot the win rates with confidence intervals
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(win_rates.keys()), y=list(win_rates.values()))
    for i, (win_rate, (lower_bound, upper_bound)) in enumerate(
        zip(win_rates.values(), confidence_intervals.values())
    ):
        plt.errorbar(
            i,
            win_rate,
            yerr=[[win_rate - lower_bound], [upper_bound - win_rate]],
            capsize=5,
            color="black",
        )
    plt.title(f"Win Rates with 95% Confidence Intervals_{bracket_name}")
    plt.xlabel("Character")
    plt.ylabel("Win Rate")
    plt.ylim(0.44, 0.6)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(
        os.path.join(
            plots_dir, f"win_rates_with_confidence_intervals_{bracket_name}.png"
        )
    )
    plt.show()


def plot_most_popular_characters(character_counts, bracket_name=""):
    # plot the most popular characters
    from pprint import pprint

    print(f"bracket_name={bracket_name}")
    pprint(character_counts)
    character_counts = Counter(character_counts)
    character_counts = dict(character_counts)
    character_counts = {
        k: v
        for k, v in sorted(
            character_counts.items(), key=lambda item: item[1], reverse=True
        )
    }
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(character_counts.keys()), y=list(character_counts.values()))
    plt.title(f"Most Popular Characters_{bracket_name}")
    plt.xlabel("Character")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, f"most_popular_characters_{bracket_name}.png"))
    plt.show()


def plot_rank_distribution(rank_counts):
    # plot the rank distribution
    rank_counts = Counter(rank_counts)
    rank_counts = dict(rank_counts)
    rank_counts = {
        f"{dan_names_dict[k]} ({k})": v
        for k, v in sorted(rank_counts.items(), key=lambda item: item[0], reverse=False)
    }
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(rank_counts.keys()), y=list(rank_counts.values()))
    plt.title("Rank Distribution")
    plt.xlabel("Rank")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "rank_distribution.png"))
    plt.show()
