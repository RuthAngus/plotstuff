import matplotlib.pyplot as plt
from colours import plot_colours
ocols = plot_colours()

def plot_params():
    plotpar = {'axes.labelsize': 18,
               'font.size': 18,
               'legend.fontsize': 18,
               'xtick.labelsize': 18,
               'ytick.labelsize': 18,
               'text.usetex': True}
    plt.rcParams.update(plotpar)
    return {'capsize':0, 'fmt':'k.', 'ecolor':'.8'}
