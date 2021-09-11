def int_input(prompt):
    while True:
        try:
            int_inp = int(input(prompt))
            return int_inp
        except ValueError as e:
            print("Not a valid integer! Try again!")



def float_input(prompt):
    while True:
        try:
            float_inp = float(input(prompt))
            return float_inp
        except ValueError as e:
            print("Not a valid floating point number! Try again!")


