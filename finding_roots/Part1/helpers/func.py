from math import *

safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                'tan', 'tanh', 'abs']

safe_dict = dict([(k, globals().get(k, None)) for k in safe_list])

def func(expr, val):
    safe_dict["x"] = val
    ans = eval(expr, {"__builtins__":None}, safe_dict)
    return ans

# expr = "abs(x) + -1*x**4"
# v = func(expr, -2)
# print(v)


