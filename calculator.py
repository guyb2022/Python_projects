from art import logo,operators
print(logo)

def print_result(first_number,operator,second_number):
    """Print the operation results of two numbers"""
    if operator == '+':
        return(first_number + second_number)
    elif operator == '-':
        return(first_number - second_number)
    elif operator == '*':
        return(first_number * second_number)
    elif operator == '/':
        if second_number != 0:
            return(first_number / second_number)
        else:
            print('Cannot divide by zero!!!')
    else:
        print("Not known operator!!!")

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
    result = print_result(first_number,operator,second_number)
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
