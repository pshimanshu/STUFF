def bairstow(coeffs, r, s, max_iters, max_rel_error):
    bs = {}, cs = {}
    n = len(coeffs)
    iters = 0
    while (iters < max_iters):
        iters+=1
        bs[n] = coeffs["a"+str(n)]
        bs[n-1] = coeffs["a"+str(n-1)] + r*bs[n]
        cs[n] = bs[n]
        cs[n-1] = bs[n-1] + r*cs[n]
        for i in range(n-2,-1,-1):
            bs[i] = coeffs["a"+str(i)] + r*bs[i+1] + s*bs[i+2]
            cs[i] = bs[i+1] + r*cs[i+1]+ s*cs[i+2]
        factor = 1/(cs[1]*cs[3]-cs[2]*cs[2])
        delr = ((cs[2]*bs[1])-(cs[3]*bs[0]))*factor
        dels = ((cs[2]*bs[0])-(cs[1]*bs[1]))*factor
        rnew = r + delr
        snew = s + dels
        er = abs(delr/rnew)
        es = abs(dels/snew)
        if (er<max_rel_error) and (es<max_rel_error):
            return 