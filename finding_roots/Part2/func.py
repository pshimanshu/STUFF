
def func(expr, val):
    ans = eval(expr, {"x":val})
    return ans

# expr = "abs(x) + -1*x**4"
# v = func(expr, -2)
# print(v)


