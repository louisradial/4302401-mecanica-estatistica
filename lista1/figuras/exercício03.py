import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
plt.rcParams.update({'font.size': 22})

COLORS = {
        "pink" : "#ea76cb",
        "mauve" : "#8839ef",
        "red" : "#d20f39",
        "yellow" : "#df8e1d",
        "green" : "#40a02b",
        "teal" : "#179299",
        "sky" : "#04a5e5",
        "sapphire" : "#209fb5",
        "blue" : "#1e66f5",
        "lavender" : "#7287fd",
        "black" : "black"
        }

SAVE_FIGURE = True
def save_figure(fig, of):
    if of is not None:
        print("[save] saving figure at " + of)
        if SAVE_FIGURE:
            fig.savefig(of, dpi=500)
            print("[save] figure saved at " + of)

def binomial_distribution(tries, successes, probability):
    return comb(tries, successes)*(probability**successes)*(1 - probability)**(tries - successes)

def gaussian_distribution(x, mean, variance):
    return 1/np.sqrt(2*np.pi*variance) * np.exp(- np.square(x - mean)/(2*variance))

def plot_binomial_gaussian(N, p, colorb, colorg):
    k = np.arange(N+1)
    x = np.linspace(0, N, num = 2000)
    b = binomial_distribution(N,k,p)
    # for i in k:
    #     b.append(binomial_distribution(N, i, p))
    g = gaussian_distribution(x, N*p, N*p*(1 - p))
    # kwargs_errorbar["ecolor"] = color
    plt.scatter(x=k/N, y=b, c=colorb, label=f"N={N}")
    plt.plot(x/N, g, c=colorg)
    # ax0.set(ylabel=ylabel)
    # ax0.grid(which='major', alpha=0.8)
    # ax0.grid(which='minor', alpha=0.2)
    # model.fit.plot_residues(ax1, data.x, data.sx)
    # ax0.tick_params(labelbottom=False)
    # ax1.grid(which='major', alpha=0.8)
    # ax1.grid(which='minor', alpha=0.2)
    # ax1.set(xlabel=xlabel)
    # ax0.set(xlim=xlims)
    # ax1.set(xlim=xlims)
    # plt.show()
    # save_figure(fig, of)


if __name__ == "__main__":
    fig = plt.figure("hi!", layout="constrained")
    # fig.suptitle("Distribuição binomial e gaussiana correspondente")
    gs = GridSpec(1,1,figure=fig)
    ax = fig.add_subplot(gs[0])
    plot_binomial_gaussian(60, 2/3, COLORS["pink"], COLORS["mauve"])
    plot_binomial_gaussian(30, 2/3, COLORS["green"], COLORS["teal"])
    plot_binomial_gaussian(15, 2/3, COLORS["blue"], COLORS["sky"])
    plt.ylabel(r"probabilidade $P_N(k)$")
    plt.xlabel(r"ocorrência relativa $\frac{k}{N}$")
    plt.xlim([0,1])
    plt.ylim([0,0.25])
    plt.legend()
    plt.grid()
    # plt.show()
    save_figure(fig, "exercício03.png")
