import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/zebrafish_publications.csv")

plt.rcParams['font.family'] = 'Avenir'

plt.figure(figsize=(14, 8), facecolor='white')

colors = {
    "Neuroscience": "#5E60CE",
    "Cancer": "#D62828",
    "Toxicology": "#2A9D8F",
    "Genetics": "#F4A261",
    "Development": "#264653"
}

markers = {
    "Neuroscience": "o",
    "Cancer": "s",
    "Toxicology": "D",
    "Genetics": "^",
    "Development": "P"
}

for topic in df["topic"].unique():

    subset = df[df["topic"] == topic]

    plt.plot(
        subset["year"],
        subset["count"],
        label=topic,
        color=colors[topic],
        linewidth=3,
        marker=markers[topic],
        markersize=7,
        markeredgecolor='black',
        markeredgewidth=0.7,
        alpha=0.95
    )

ax = plt.gca()

ax.set_facecolor("#FAFAFA")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

plt.grid(
    True,
    linestyle='--',
    linewidth=0.6,
    alpha=0.35
)

plt.xlabel(
    "Year",
    fontsize=15,
    labelpad=12
)

plt.ylabel(
    "Number of Publications",
    fontsize=15,
    labelpad=12
)

plt.title(
    "Evolution of Zebrafish Research Across Biological Disciplines",
    fontsize=22,
    fontname='Avenir',
    pad=22
)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

legend = plt.legend(
    frameon=True,
    fancybox=True,
    fontsize=11,
    borderpad=1
)

legend.get_frame().set_alpha(0.9)

plt.tight_layout()

plt.savefig(
    "plots/zebrafish_publication_trends_publication_ready.png",
    dpi=600,
    bbox_inches='tight'
)

plt.show()