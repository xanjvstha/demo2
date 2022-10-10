# 1. Core Python
# 1. Write a program which prints “Hello World of Python”.
print("Hello World of Python")

# 2. Write a program which prints your personal information (person id, full name, contact address).
print("9851225093")
print("Sanjeev Shrestha")
print("Budhanilkantha-11, Kathmandu")

# 3. Write a program which accepts personal information and displays (person id, full name, contact address).
personid = input("Enter Person ID:")
fullname = input("Enter Fullname:")
address = input("Enter Contact Address:")
print("Person ID: - ", personid)
print("Full Name: - ", fullname)
print("Contact Address: - ", address)

# 4. Write a program to print sum, difference, product, division, power of two numbers which input from the user
num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))
print("First number is", num1)
print("Second number is", num2)
print("-------------------------------------")
add: int = num1 + num2
print("Addition of two number is:", add)
sub = num1 - num2
print("Subtraction of two number is:", sub)
mul = num1 * num2
print("Multiplication of two number is:", mul)
div = num1 / num2
print("Division of two number is:", div)
pow = num1 + num2
print("Modulus of two number is:", pow)

# 5. Write a program to convert temperatures to and from celsius, fahrenheit.
temperature = input("Enter the  temperature celsius or fahrenheit ? (e.g., 45F, 102C etc.) : ")
degree = int(temperature[:-1])
convention = temperature[-1]

if convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    convent = "Fahrenheit"
elif convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    convent = "Celsius"
else:
    print("Input proper convention.")
    quit()
print("The temperature in", convent, "is", result, "degrees.")

# 6. Write a program to guess a number between 1 to 9.
import random

target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

# 7. Write a program that accepts a word from the user and reverse it.
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n")

# 8. write a program to calculate simple interest
print("Enter the Principle Amount: ")
p = int(input())
print("Enter Rate of Interest (%): ")
r = float(input())
print("Enter Time Period: ")
t = float(input())
si = (p * r * t) / 100
print("\nSimple Interest Amount: ")
print(si)

# 9. Write a program to calculate compound interest.
p = float(input("Enter the principal amount : "))

t = float(input("Enter the number of years : "))

r = float(input("Enter the rate of interest : "))

ci = p * (pow((1 + r / 100), t))

print("Compound interest : {}".format(ci))

# 10. Write a program to check Armstrong Number.

# take input from the user
num = int(input("Enter a number: "))

sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# 11. Write a program to check whether a number is Prime or not.

n = 5

# Check if the number is greater than 1

if n > 1:
    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            print(num, "is not a prime number")
        break
    else:
        print(n, "is a prime number")
# If the number is less than 1, its also not a prime number.
else:
    print(n, "is not a prime number")

# 12. Write a program to calculate the area of a circle.
from math import pi

r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))

# 13. Write a program to print the ASCII value of a character.
c = 'p'
print("The ASCII value of a character'" + c + "' is", ord(c))

# 14. Write a program to swap two numbers.
# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# 2. If Statement
# 18. Write a program to check whether a person is eligible for voting or not.
age = input("Enter the Age:")
age = int(age)

if age <= 18:
    print("Not Eligible for Voting")
else:
    print("Eligible for Voting")

# 19. Write a program to check whether the number entered by the user is even or odd.
number = int(input("Enter any number: - "))
number = number / 2
print(number)
if number % 2 == 0:
    print("Entered number is Even.")
else:
    print("Entered number is Odd.")

# 19. Write a program to check whether a number is divisible by 7 or not.
num3 = int(input("Enter number: - "))
print(num3)
last_number = int(repr(num3)[-1]) % 7 == 0
print(f"The last number of {num3} is {last_number}.")
if num3 % 7 == 0 and num3 != 0:
    print("Divisible by 7.")
else:
    print("Not Divisible by 7")

# 20. Write a program to display "Hello" if a number entered by the user is a multiple of five, otherwise print "Bye".
num = int(input("Enter your number: "))

if num % 5 == 0:

    print("Hello")

else:

    print("Bye")

# 21. Write a program to display the last digit of a number.
num2 = int(input("Enter number: - "))
print(num2)
last_number = int(repr(num2)[-1])
print(f"The last number of {num2} is {last_number}.")

# 22. Write a program to check whether the last digit of a number is divisible by 3 or not.
num = int(input("Enter a number:"))
last_digit = num % 10
if last_digit % 3 == 0:
    print("{} is divisible by 3 ".format(last_digit))
else:
    print("{} is not divisible by 3".format(last_digit))

# 23. Write a program to check whether a year is a leap year or not.
year = int(input("Enter year: - "))
print(year)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year.")

# 24. Write a program to check if a given number is a Fibonacci number
n = int(input("Enter the number: "))
c = 0
a = 1
b = 1
if n == 0 or n == 1:
    print("Yes")
else:
    while c < n:
        c = a + b
        b = a
        a = c
    if c == n:
        print("This is a Fibonacci Number")
    else:
        print("This is not a Fibonacci Number")

# 25. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 7 for Saturday.
day = input("Enter value (1-7):")
day = int(day)

if day <= 0 or day >= 13:
    print("Out of Range")
if day == 1:
    print("SUNDAY")
if day == 2:
    print("MONDAY")
if day == 3:
    print("TUESDAY")
if day == 4:
    print("WEDNESDAY")
if day == 5:
    print("THURSDAY")
if day == 6:
    print("FRIDAY")
if day == 7:
    print("SATURDAY")

# 28. Write a program to check whether a person is a senior citizen or not.
age = int(input("Enter the age of the person: "))
if age >= 60:
    status = " Senior citizenship"
else:
    status = " Not a senior citizenship"

print(" The person is ", status)


