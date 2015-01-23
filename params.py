import matplotlib.pyplot as plt
from colours import plot_colours
ocols = plot_colours()

def plot_params():
    plotpar = {'axes.labelsize': 12,
               'text.fontsize': 10,
               'legend.fontsize': 15,
               'xtick.labelsize': 12,
               'ytick.labelsize': 12,
               'text.usetex': True}
    plt.rcParams.update(plotpar)
    return {'capsize':0, 'fmt':'k.', 'ecolor':'.8'}
