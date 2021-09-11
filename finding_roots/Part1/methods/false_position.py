from helpers.func import func as f


def false_position(expression, left, right, max_iters, max_rel_error):
    errors = []
    iterations = []
    fleft = f(expression, left)
    fright = f(expression, right)
    if fleft*fright > 0:
        return None, errors, iterations
    pos = (right*fleft - left*fright)/(fleft - fright)
    old_pos = pos+1000
    iters = 0
    while (iters < max_iters):
        iters+=1
        iterations.append(iters)
        if iters!=1:
            old_pos = pos  
        fleft = f(expression, left)
        fright = f(expression, right)        
        pos = (right*fleft - left*fright)/(fleft - fright)
        fpos = f(expression, pos)
        if (fpos==0):
            errors.append(0)
            return pos, errors, iterations
        if (fleft*fpos > 0):
            left = pos
        else:
            right = pos
        e = abs((pos-old_pos)/pos)*100
        errors.append(e)
        if (e <= max_rel_error):
            return pos, errors, iterations
    return pos, errors, iterations




# expr = "600*x^4 - 20*x^3+19x -5"
# left = 0.1
# right = 1.0
# max_iters = 20
# max_rel_error = 0.05
# root = false_position(expr, left, right, max_iters, max_rel_error)
# print(root)