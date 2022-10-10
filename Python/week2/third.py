# create a program - filename.py
# run program
# variable declare and initialize
import math

# num1 = None
# accept input
# num1 = input("Enter any number: - ")
#
# num1 = 5 # Simple assignment operator
# num1 = num2 = num3 = 5 # Multiple assignment operator
# num4 += 1 # Short-hand assignment operator

# arithmetic operator
# +, -, *, /, %, //, **, math.pow, math.sqrt

# Relational Operator
# ==, !=, >, <, >=, <=

# Logical Operator
# AND, OR, NOT

# Other Operators
# [], {}, (), ., ,

# Operator Precedence and Associativity
# ?

# Unit -2
# Basic IO
# Reading value from Keyboard
# Printing value on display

# Unit -3 Control Statements
# if statement
# num1 = 0
# if num1 == 0:
#     print("Hello")
# if num1 != 0:
#     print("Hi")

# if ... else statement
# num1 = 0
# if num1 == 0:
#     print("Hello")
# else:
#     print("Hi")

# if ... elif statement
#
# num1 = 0
# if num1 == 0:
#     print("Zero")
# elif num1 == 1:
#     print("One")
# elif num1 == 2:
#     print("Two")
# else:
#     print("Others")

# Nested if
# num1 = 5
# num2 = 7
# num3 = 6
#
# if num1 > num2:
#     if num1 > num3:
#         print(num1)

# if statement with multiple condition
# num1 = 5
# num2 = 6
# num3 = 3
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# elif num3 > num1 and num3 > num2:
#     print(num3)

# NOT operator
# result = True
# print(not result)

# Looping statement
# Loop design
# start
# stop
# condition
# statement
# modifier

# Print 1 to 10
# start = 1
# stop = 10
# condition = start<=stop
# statement = print(start)
# modifier = start +=1

# start = 1
# stop = 10
# while start <= stop:
#     print(start, end=',')
#     start += 1

# Print 10 to 1
# start = 10
# stop = 1
# condition = start>=stop
# statement = print(start)
# modifier = start -=1
# start = 10
# stop = 1
# while start >= stop:
#     print(start, end=',')
#     start -= 1

# print sum of 1 to 10
start = 1
stop = 10
sum = 0
while start<=stop:
    sum += start
    sum += 1
print(sum)

# print sum of 10 to 1
start = 10
stop = 1
while start>=stop:
    sum += start
    start-=1
print(sum)