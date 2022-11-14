#Calculator
logo = """
 _____________________
|  _________________  |
| | AishShyam   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

print(logo)


def calculation():
    num1 = float(input("First number? "))
    num2 = float(input("Second number? "))
    for item in operations:
        print(item)
    operation_symbol = input("Pick an operator from above ")

    # if operation_symbol == "+":
    #   answer = add(num1,num2)
    # elif operation_symbol == "-":
    #   answer = subtract(num1,num2)
    # elif operation_symbol == "*":
    #   answer = multiply(num1, num2)
    # else:
    #   answer = divide(num1, num2)
    more_calculations = True

    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    go_on = input("Do you want to continue? y or n: ").lower()

    if go_on == "n":
        more_calculations = False
        print(f"Total: {first_answer}")
        calculation()

    while more_calculations:
        operation_symbol = input("Pick next operator ")
        calculation_function = operations[operation_symbol]
        num3 = float(input("Next number? "))
        second_answer = calculation_function(first_answer, num3)
        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        go_on = input("Do you want to continue? y or n: ").lower()
        if go_on == "n":
            more_calculations = False
            print(f"Total: {second_answer}")
            calculation()


calculation()

