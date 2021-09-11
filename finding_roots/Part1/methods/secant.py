from helpers.func import func as f


def secant(expression, left, right, max_iters, max_rel_error):
    errors = []
    iterations = []
    fleft = f(expression, left)
    fright = f(expression, right)
    if fleft*fright > 0:
        return None, errors, iterations
    intermediate = right - (fright*(right-left))/(fright-fleft)
    iters = 0
    while (iters < max_iters):
        iters+=1
        iterations.append(iters)
        fleft = f(expression, left)
        fright = f(expression, right)
        intermediate = right - (fright*(right-left))/(fright-fleft)
        left = right
        right = intermediate
        e = abs(f(expression, intermediate))
        errors.append(e)
        if (e <= max_rel_error):
            return intermediate, errors, iterations
        #print("iter: {}, left: {}, right: {}, intermediate: {}".format(iters, left, right, intermediate))
    return intermediate, errors, iterations




# expr = "600*x^4 - 20*x^3+19*x -5"
# expr = expr.replace("^", "**")
# left = 0.1
# right = 1.0
# max_iters = 20
# max_rel_error = 0.05
# root = secant(expr, left, right, max_iters, max_rel_error)
# print(root)