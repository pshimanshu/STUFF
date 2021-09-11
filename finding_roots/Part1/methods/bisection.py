from helpers.func import func as f


def bisection(expression, left, right, max_iters, max_rel_error):
    errors = []
    iterations = []
    fleft = f(expression, left)
    fright = f(expression, right)
    if fleft*fright > 0:
        return None, errors, iterations
    iters = 0
    while (iters < max_iters):
        iters+=1
        iterations.append(iters)
        mid = (left+right)/2
        fmid = f(expression, mid)
        if (fmid==0):
            errors.append(0)
            return mid, errors, iterations
        fleft = f(expression, left)
        if (fmid*fleft > 0):
            left = mid
        else:
            right = mid
        e = abs(fmid)
        errors.append(round(e,3))
        if (e <= max_rel_error):
            return mid, errors, iterations
    return mid, errors, iterations


# expr = "600*x^4 - 20*x^3+19*x -5"
# expr = expr.replace("^", "**")
# left = 0.1
# right = 1.0
# max_iters = 20
# max_rel_error = 0.05
# root, errors, iterations = bisection(expr, left, right, max_iters, max_rel_error)
# print(root, errors, iterations)
# plt.scatter(iterations, errors)
# plt.xticks()
# plt.xlabel('ITERATIONS')
# plt.xlim([1, iterations[-1]])
# plt.ylabel('ERRORS')
# plt.show()
