# n = int(input("Enter the degree of the polynomial: "))

# coeffs = {}
# fx = ""
# for i in range(n, -1, -1):
#     coeffs["a"+str(i)] = float(input("Enter the coefficient of x^{}".format(i)))
#     if str(coeffs["a"+str(i)])[0]!='-':
#         fx += " + "
#     fx += str(coeffs["a"+str(i)]) + "x^" + str(i) + " "

# print(fx)
from take_inputs import int_input, float_input
from muller import muller


print("Attempting to solve the roots of a polynomial equation using any of the 2 following mentioned methods....")
print("---"*45)


expression = input("Enter the non-linear equation: ")
expression = expression.replace("^", "**")

DNE = "does not exist"

while True:
    method = int(input("Select the method of computation of finding roots of a polynomial equation f(x):\n\t 1. Muller Method\n\t 2. Bairstow Method \n \t 3. Exit\n"))
    if method==1:
        a = int_input("Enter the first guess: ")
        b = int_input("Enter the second gues: ")
        c = int_input("Enther the third guess: ")
        max_iters = int_input("Enter the maximum number of iterations: ")
        max_rel_error = float_input("Enter the maximum relative approximate error (in %): " )/100
        root = muller(expression, a, b, c, max_iters, max_rel_error)
        if root==None:
            print("Root for given non-linear equation, {}, {} with the inital guesses, {:.2f}, {:.2f} and {:.2f}".format(expression, DNE, a, b, c));
        else:
            print("Root for given non-linear equation, {}, with the inital guesses, {:.2f}, {:.2f} and {:.2f} is {:.2f}".format(expression, a, b, c, root))
        print("---"*45)
    elif method==2:
        print("Wasn't able to complete this method.")
        pass
    elif method==3:
        print("Thank you for using our program!!\nGoodbye!")
        print("---"*45)
        break
    else:
        print("Invalid Selection, please select again")