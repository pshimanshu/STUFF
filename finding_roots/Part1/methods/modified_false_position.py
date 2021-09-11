from helpers.func import func as f


def modified_false_position(expression, left, right, max_iters, max_rel_error):
    errors = []
    iterations = []
    fl = f(expression, left)
    fr = f(expression, right)/2
    if fl*fr > 0:
        return None, errors, iterations
    pos = (right*fl - left*fr)/(fl - fr)
    old_pos = pos+1000
    iters = 0
    factor = 0
    while (iters < max_iters):
        iters+=1
        iterations.append(iters)
        fl = f(expression, left)
        fr = f(expression, right)        
        pos = (right*fl - left*fr)/(fl - fr)
        fpos = f(expression, pos)
        if (fpos==0):
            errors.append(0)
            return pos, errors, iterations
        if (fl*fpos < 0):
            factor = abs(2*fpos/(right-pos))+1
            mod_pos = (factor*left*fr-right*fl)/(factor*fr - fl)
            fmod_pos = f(expression, mod_pos)
            if fmod_pos*fl<0:
                right = mod_pos
            else:
                right = pos
                left = mod_pos
        else:
            factor = abs(0.5*fpos/(right-pos))+1
            mod_pos = (factor*right*fl-left*fr)/(factor*fl - fr)
            fmod_pos = f(expression, mod_pos)
            if fmod_pos*fl>0:
                left = mod_pos
            else:
                left = pos
                right = mod_pos
        e = abs(f(expression, mod_pos))
        errors.append(e)
        if (e <= max_rel_error):
            return pos, errors, iterations
    return pos, errors, iterations



# expr = "600*x**4 - 20*x**3+19*x -5"
# left = 0.1
# right = 1.0
# max_iters = 20
# max_rel_error = 0.05
# root = modified_false_position(expr, left, right, max_iters, max_rel_error)
# print(root)