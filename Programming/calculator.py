## Program of menu based calculator
import os
def add(num1, num2):
    return(num1 + num2)
def subtract(num1, num2):
    return(num1 - num2)
def multiply(num1, num2):
    return(num1 * num2)
def divide(num1, num2):
    return(num1/num2)

while 1:
    os.system('clear')
    print("This is  menu for calculator")
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 0 for exit")
    option = int(input("Enter your choice: "))
    if option == 0:
        break
    if option > 4 or option < 0:
        print("You have entered wrong choice")
        continue
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = 0
    if option == 1:
        result = add(num1, num2)
        print("Result of addition is ",result)
    elif option ==  2:
        result = subtract(num1, num2)
        print("Result of subtrction is  ",result)
    elif option == 3:
        result = multiply(num1, num2)
        print("Result of multiplication is ",result)
    elif option == 4:
        result = divide(num1, num2)
        print("Result of division is ",result)
    else:
        print("You have entered wrong choice")
    input("Press enter to continue: ")



    

   
