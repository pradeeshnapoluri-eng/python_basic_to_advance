def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def exponent(a,b):
    return a^b
def floor_division(a,b):
    return a//b
performing_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^":exponent,
    "//": floor_division,
    }
num1 = int(input("Enter first number: "))
for operator in performing_operations:
    print(operator)
continue_performance = True
while continue_performance:
    symbol = input("Enter your choice of operation: ")
    num2 = int(input("Enter second number: "))
    calculation = performing_operations[symbol]
    print(calculation)
    result = calculation(num1,num2)
    print(f"{num1} {symbol} {num2} = {result}")
    print(f"your result is {result},got executed successfully.")
    want_continue = input(f"Would you like to continue the {result} or not? (y/n)? ")
    if want_continue == "y":
        num1 = result
    else:
        continue_performance = False
        print("Thank you for the exit!")
###########################################################################################################################################
#here the calculator code has for loop,while loop,if else statements.1st defining all the operations.
#then we want user input function.after that to iterate the dictionary of the operations,we use for loop.
#after that,to continue the process along with answer we use True operation.this is ON operation in system.
#afetr that we use while loop.here we want the another choice of operation and also with the 2nd user input.
#in calculation variable,we store that value which printed after the output of 1st iteration.
#last we wrote if-else statements.here if u want to exit the code we use else statement.we used False to exit out of the loop.

