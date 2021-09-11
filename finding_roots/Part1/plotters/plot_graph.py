from helpers.func import func as f

import matplotlib.pyplot as plt
import numpy as np

def plot_graph(left_limit_x, right_limit_x, expresion):
    left_limit_x = int(left_limit_x)
    right_limit_x = int(right_limit_x)
    xvs = np.linspace(left_limit_x, right_limit_x, (right_limit_x-left_limit_x)*2)
    yvs = np.array(list([f(expresion, x)] for x in xvs))
    plt.scatter(xvs, yvs)
    plt.plot(xvs, yvs)
    plt.axhline(y = 0, color = 'r', linestyle = '-')
    plt.xlabel("x")
    plt.ylabel("f(x) = " + expresion)
    plt.show()
    #figure.tight_layout()

# xll = 2
# xrl = 5
# expr = "2*x**2"
# plot_graph(xll, xrl, expr)