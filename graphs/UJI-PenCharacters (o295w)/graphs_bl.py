import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

s = StringIO(""" dist acc fscore prot appb appw buffb buffw
PV-AB 37.68 0.83 0.80 0.44 0.059 0.092 0.019 0.004
PV-A 36.62 0.78 0.76 0.41 0.018 0.030 NaN NaN
PV 56.30 0.82 0.80 0.39 NaN NaN NaN NaN
PV-B 57.60 0.86 0.82 0.42 NaN NaN 0.078 0.120
BL 55.80 0.86 0.82 0.38 NaN NaN NaN NaN""")

df = pd.read_csv(s, index_col=0, delimiter=' ', skipinitialspace=True)
df = df.astype(float)

fig = plt.figure(figsize=(7, 4), dpi=80)   # Create matplotlib figure

ax = fig.add_subplot(111)  # Create matplotlib axes
ax.set_ylim(0, 80)
ax2 = ax.twinx()
ax2.set_ylim(0, 1)
ax3 = ax.twinx()
ax3.set_ylim(0, 0.12)

# right, left, top, bottom
ax3.spines['right'].set_position(('outward', 60))

# no x-ticks
ax3.xaxis.set_ticks([])

width = 0.15

df.dist.plot(kind='bar', color='#0084a3', ax=ax, width=width, position=3, rot=0)
df.acc.plot(kind='bar', color='#f9c768', ax=ax2, width=width, position=2, rot=0)
df.fscore.plot(kind='bar', color='#70507a', ax=ax2, width=width, position=1, rot=0)
df.prot.plot(kind='bar', color='#9bd670', ax=ax2, width=width, position=0, rot=0)
df.appb.plot(kind='bar', color='#cf4931', ax=ax3, width=width, position=-1, rot=0)
df.appw.plot(kind='bar', color='#ffa05c', ax=ax3, width=width, position=-2, rot=0)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(["PV-AB", "PV-A", "PV", "PV-B", "$\\it{BL}$"])

# ask matplotlib for the plotted objects and their labels
lines, _ = ax.get_legend_handles_labels()
lines2, _ = ax2.get_legend_handles_labels()
lines3, _ = ax3.get_legend_handles_labels()
ax.legend(lines + lines2 + lines3, ["Dist. (x100)", "Acc.", "$F_1$", "Prot.", "App.$\\uparrow$",
                                    "App.$\\downarrow$"], ncol=3, loc=(0.001, 1.0))

ax.set_ylabel('Dist.')
ax2.set_ylabel('Acc. / $F_1$ / Prot.')
ax3.set_ylabel('App.$\\uparrow$ / App.$\\downarrow$')
plt.xlim(-0.65, 4.6)
fig.savefig('o295w_bl.png', bbox_inches='tight', facecolor=fig.get_facecolor(), transparent=True)

plt.show()
