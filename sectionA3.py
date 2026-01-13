num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num3=float(input("enter the third number:"))
if num1>=num2 and num1>=num3:
    print("num1 largest number")
elif num2<=num1 and num2<=num3:
    print("num2 largest number")
else:
    print("num3 largest number")
