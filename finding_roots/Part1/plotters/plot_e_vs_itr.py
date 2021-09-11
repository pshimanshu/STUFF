import matplotlib.pyplot as plt

def plot_e_vs_itr(errors, iterations):
    plt.scatter(iterations, errors)
    plt.xticks()
    plt.xlabel('ITERATIONS')
    plt.xlim([0, iterations[-1]+1])
    plt.axhline(y = 0, color = 'r', linestyle = '-')
    plt.ylabel('ERRORS')
    plt.show()
