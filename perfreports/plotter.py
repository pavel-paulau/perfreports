import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'font.size': 5})
matplotlib.rcParams.update({'lines.linewidth': 0.5})
matplotlib.rcParams.update({'lines.marker': '.'})
matplotlib.rcParams.update({'lines.markersize': 3})
matplotlib.rcParams.update({'lines.linestyle': 'None'})
matplotlib.rcParams.update({'axes.linewidth': 0.5})
matplotlib.rcParams.update({'axes.grid': True})
matplotlib.rcParams.update({'axes.formatter.limits': (-6, 6)})
matplotlib.rcParams.update({'legend.numpoints': 1})
matplotlib.rcParams.update({'legend.fancybox': True})
matplotlib.rcParams.update({'legend.markerscale': 1.5})
matplotlib.rcParams.update({'legend.loc': 0})
matplotlib.rcParams.update({'legend.frameon': True})
import matplotlib.pyplot as plt

from perfreports.constants import PALETTE


def plot(series, ylabel, fname):
    fig = plt.figure(figsize=(4.66, 2.625))

    ax = fig.add_subplot(*(1, 1, 1))
    ax.ticklabel_format(useOffset=False)
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Time elapsed, sec')
    ax.plot(series.index, series, color=PALETTE[0])

    ymin, ymax = ax.get_ylim()
    plt.ylim(ymin=0, ymax=max(1, ymax * 1.05))

    fig.tight_layout()
    fig.savefig(fname, dpi=200)
    plt.close()
