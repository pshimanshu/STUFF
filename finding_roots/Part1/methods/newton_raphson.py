from helpers.func import func as f


def newton_raphson(fexpr, dfexpr, start, max_iters, max_rel_error):
    iters = 0
    errors = []
    iterations = []
    while (iters < max_iters):
        iters+=1
        iterations.append(iters)
        fstart = f(fexpr, start)
        e = abs(fstart)
        errors.append(e)
        if (e <= max_rel_error):
            return start, errors, iterations
        dfstart = f(dfexpr, start)
        if dfstart==0:
            print("Derivate of function becomes 0")
            return None, errors, iterations        
        start -= (fstart/dfstart)
    return start, errors, iterations




# fexpr = "600*x^4 - 20*x^3+19*x -5"
# dfexpr = "2400*x^3 - 60*x^2 + 19"
# fexpr = fexpr.replace("^", "**")
# dfexpr = dfexpr.replace("^", "**")

# start = 0.5
# max_iters = 20
# max_rel_error = 0.05
# root = newton_raphson(fexpr, dfexpr, start, max_iters, max_rel_error)
# print(root)