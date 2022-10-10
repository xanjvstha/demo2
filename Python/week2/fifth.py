# num1=int(input("Enter a first number:"))
# num2=int(input("Enter a second number:"))
# print("First number is",num1)
# print("Second number is",num2)
# print("-------------------------------------")
# add=num1+num2
# print("Addition of two number is:",add)
# sub=num1-num2
# print("Subtraction of two number is:",sub)
# mul=num1*num2
# print("Multiplication of two number is:",mul)
# div=num1/num2
# print("Division of two number is:",div)
# pow=num1+num2
# print("Modulus of two number is:",pow)
# 
n = int(input("Enter the number: "))
c = 0
a = 1
b = 1
if n == 0 or n == 1:
    print("This is a Fibonacci Number")
else:
    while c < n:
        c = a + b
        b = a
        a = c
    if c == n:
        print("This is a Fibonacci Number")
    else:
        print("This is not a Fibonacci Number")