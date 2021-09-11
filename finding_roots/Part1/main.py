import sys
import os

os.system('pip3 install matplotlib --quiet')
os.system('pip3 install numpy --quiet')
from matplotlib import pyplot as plt
import numpy as np
#os.system('pip3 install ')
#import colorama


from helpers.take_inputs import int_input, float_input

from methods.bisection import bisection
from methods.false_position import false_position
from methods.modified_false_position import modified_false_position
from methods.newton_raphson import newton_raphson
from methods.secant import secant

from plotters.plot_e_vs_itr import plot_e_vs_itr
from plotters.plot_graph import plot_graph


print("Attempting to solve the roots of a non-linear expression using any of the 5 following mentioned methods....")
print("---"*45)

expression = input("Enter the non-linear equation: ")
expression = expression.replace("^", "**")
#print(expression)

DNE = "does not exist"
#DNE = colored('does not exist', 'red', attrs=['reverse', 'blink'])

while True:
    method = int(input("Select the method of computation of finding roots of a non-linear equation f(x):\n\t 1. Bisection Method\n\t 2. False-Position Method\n\t 3. Modified False-Position Method\n\t 4. Newton-Raphson Method\n\t 5. Secant Method\n\t 6.Exit\n"))
    if method==1:
        left = float_input("Enter the left limit of initial interval: ")
        right = float_input("Enter the right limit of initial interval: ")
        max_iters = int_input("Enter the maximum number of iterations: ")
        max_rel_error = float_input("Enter the maximum relative approximate error (in %): " )/100
        root, errors, iterations = bisection(expression, left, right, max_iters, max_rel_error)
        disp = (right-left)/4
        plot_graph(left-disp, right+disp, expression)
        print("--"*35)
        print("Solving the roots of '{}' using 'Bisection Method'".format(expression))
        if root==None:
            print("Root for given non-linear equation, {}, {} in the interval [{:.2f}, {:.2f}]".format(expression, DNE, left, right))
        else:
            print("Root for given non-linear equation, {}, in the interval [{:.2f}, {:.2f}] is {:.2f}".format(expression, left, right, root))
            plot_e_vs_itr(errors, iterations)
        print("---"*45)
    elif method==2:
        left = float_input("Enter the left limit of initial interval: ")
        right = float_input("Enter the right limit of initial interval: ")
        max_iters = int_input("Enter the maximum number of iterations: ")
        max_rel_error = float_input("Enter the maximum relative approximate error (in %): " )/100
        root, errors, iterations = false_position(expression, left, right, max_iters, max_rel_error)
        disp = (right-left)/4
        plot_graph(left-disp, right+disp, expression)
        print("--"*35)
        print("Solving the roots of '{}' using 'False-Position Method'".format(expression))        
        if root==None:
            print("Root for given non-linear equation, {}, {} in the interval [{:.2f}, {:.2f}]".format(expression, DNE, left, right))
        else:
            print("Root for given non-linear equation, {}, in the interval [{:.2f}, {:.2f}] is {:.2f}".format(expression, left, right, root))
            plot_e_vs_itr(errors, iterations)
        print("---"*45)
    elif method==3:
        left = float_input("Enter the left limit of initial interval: ")
        right = float_input("Enter the right limit of initial interval: ")
        max_iters = int_input("Enter the maximum number of iterations: ")
        max_rel_error = float_input("Enter the maximum relative approximate error (in %): " )/100
        root, errors, iterations = modified_false_position(expression, left, right, max_iters, max_rel_error)
        disp = (right-left)/4
        plot_graph(left-disp, right+disp, expression)
        print("--"*35)
        print("Solving the roots of '{}' using 'Modified False-Position Method'".format(expression))        
        if root==None:
            print("Root for given non-linear equation, {}, {} in the interval [{:.2f}, {:.2f}]".format(expression, DNE, left, right))
        else:
            print("Root for given non-linear equation, {}, in the interval [{:.2f}, {:.2f}] is {:.2f}".format(expression, left, right, root))
            plot_e_vs_itr(errors, iterations)
        print("---"*45)
    elif method==4:
        derivate_expression = input("Enter the derivative of the non-linear equation: ")
        derivate_expression = derivate_expression.replace("^", "**")
        start = float_input("Enter the initial guess of the root to given equation: ")
        max_iters = int_input("Enter the maximum number of iterations: ")
        max_rel_error = float_input("Enter the maximum relative approximate error (in %): " )/100
        root, errors, iterations = newton_raphson(expression, derivate_expression, start, max_iters, max_rel_error)
        plot_graph(start-8, start+8, expression)
        print("--"*35)
        print("Solving the roots of '{}' using 'Newton-Raphson Method'".format(expression))
        if root==None:
            print("Root for given non-linear equation, {}, {} in the interval [{:.2f}, {:.2f}]".format(expression, DNE, left, right))
        else:
            print("Root for given non-linear equation, {}, in the interval [{:.2f}, {:.2f}] is {:.2f}".format(expression, left, right, root))
            plot_e_vs_itr(errors, iterations)
        print("---"*45)
    elif method==5:
        left = float_input("Enter the left limit of initial interval: ")
        right = float_input("Enter the right limit of initial interval: ")
        max_iters = int_input("Enter the maximum number of iterations: ")
        max_rel_error = float_input("Enter the maximum relative approximate error (in %): " )/100
        root, errors, iterations = secant(expression, left, right, max_iters, max_rel_error)
        disp = (right-left)/4
        plot_graph(left-disp, right+disp, expression)
        print("--"*35)
        print("Solving the roots of '{}' using 'Secant Method'".format(expression))
        if root==None:
            print("Root for given non-linear equation, {}, {} in the interval [{:.2f}, {:.2f}]".format(expression, DNE, left, right))
        else:
            print("Root for given non-linear equation, {}, in the interval [{:.2f}, {:.2f}] is {:.2f}".format(expression, left, right, root))
            plot_e_vs_itr(errors, iterations)
        print("---"*45)
    elif method==6:
        print("Thank you for using our program!!\nGoodbye!")
        print("---"*45)
        break
    else:
        print("Invalid Selection, please select again")
