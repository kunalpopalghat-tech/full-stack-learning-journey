# WAP to add three  numbers and return sum to caller .Display sum from global scope. you may use input function and type casting.

def add_numbers():
    num1 = eval(input("Enter first number"))
    num2 = eval(input("Enter second number"))
    num3 = eval(input("Enter third number"))
    
    sum = num1 + num2 + num3

    return sum


res = add_numbers()

print("sum =", res)
