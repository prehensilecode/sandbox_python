#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
ax = sns.histplot(data=penguins, x="flipper_length_mm")
plt.savefig("seaborn_plot.png")
