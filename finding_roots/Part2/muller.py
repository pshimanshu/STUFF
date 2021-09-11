import math

from func import func as f

def muller(expression, a, b, c, max_iters, max_rel_error):
    iters = 0
    xnew = 0
    while (iters < max_iters):
        iters+=1
        print(iters, xnew)
        fa = f(expression, a)
        fb = f(expression, b)
        fc = f(expression, c)
        h1, h2 = b-a, c-b
        d1, d2 = (fb-fa)/h1, (fc-fb)/h2
        a0 = (d2-d1)/(h2+h1)
        a1 = a0*h2 + d2
        a2 = fc
        discr = abs(math.sqrt(a1*a1-4*a0*a2))
        x, y = -2*a0/(a1+discr) , -2*a0/(a1-discr)
        if (x>=y):
            xnew = x+c
        else:
            xnew = y+c
        if (abs(xnew-c) < max_rel_error):
            return xnew
        a = b
        b = c
        c = xnew
    return xnew




expr = "600*x^4 - 550*x^3 + 200*x^2 - 20*x -1"
# expr = "x^3 + x^2 - 4*x - 4"
expr = expr.replace("^", "**")
x0, x1, x2 = 0, 0.1, 0.3
# x0, x1, x2 = 0, 0.5, 1
max_iters = 20
max_rel_error = 0.05
root = muller(expr,x0, x1, x2, max_iters, max_rel_error)
print(root)