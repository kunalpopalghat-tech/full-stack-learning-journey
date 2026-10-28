# Write a Python program to find the largest number among three numbers entered by the user.
num1 = int(input("Enter your first number = "))
num2 = int(input("Enter your second number = "))
num3 = int(input("Enter your third number = "))

if num1 > num2 and num1 > num3:
    print(f"Largest number is: {num1}")

elif num2 > num1 and num2 > num3:
    print(f"Largest number is: {num2}")

else:
    print(f"Largest number is: {num3}")
