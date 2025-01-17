def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
import art
def calculate_():
    print(art.logo)
    over = False
    n1 = float(input("Enter the first number : "))
    operation = input("choose your operation '+' ,'-' ,'*' ,'/'  : ")
    n2 = float(input("Enter the second number : "))
    calculate = {"+":add , "-" : subtract , "*" : multiply , "/" : divide}
    result = calculate[operation] (n1,n2)
    print(result)
    while not over :
        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if to_continue == "y":
            operation = input("choose your operation '+' ,'-' ,'*' ,'/'  : ")
            n2 = float(input("Enter the second number : "))
            result = calculate[operation](result, n2)
            print(result)
            over = False
        else :
            over = True
            print("\n"*20 )
            calculate_()
calculate_()




