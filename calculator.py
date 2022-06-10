from art import logo,operators
print(logo)

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

operator_sign = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
}

def calc_result(first_number,operator,second_number):
    """Print the operation results of two numbers"""
    calculation_function = operator_sign[operator]
    return calculation_function(first_number, second_number)
    
def get_user_inputs(mode, last_number = None):
    """Get the inputs from the user
       Need to seperate between two options:
       1. using last value
       2. starting from the begining
    """
    if not mode:
        first_number = int(input("What's the first number? "))
        print(operators)
    else:
        first_number = last_number
    operator = input('Pick an operation: ')
    second_number = int(input("What's the next number? "))
    result = calc_result(first_number,operator,second_number)
    print(f"{first_number} {operator} {second_number} = {result}")
    return result
    
mode = 0
not_end = True
while not_end:
    if mode == 0:
        result = get_user_inputs(mode)
    choice = input(f"Type 'Y' to use last value {result} \n or 'n' to start from begining \n Press 'e' to exit. ")
    if choice.lower() == 'e':
        not_end = False
    elif choice.lower() == 'y':
        mode = 1
        result = get_user_inputs(mode,result)
    elif choice.lower() == 'n':
        mode = 0

print("End of this Program")
