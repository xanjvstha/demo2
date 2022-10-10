# write a program to check whether the number is even or odd number.
number = int(input("Enter any number: - "))
number = number/2
print(number)
if number % 2 == 0:
    print("Entered number is Even.")
else:
    print("Entered number is Odd.")

# write a program to check whether the number is positive or negative or zero
# num1 = float(input("Enter number: -"))
# print(num1)
# if num1 > 0:
#     print("Entered number is Positive.")
# elif num1 == 0:
#     print("Entered number is Zero.")
# else:
#     print("Entered number is Negative.")

# Program to display last digit of number.
num2 = int(input("Enter number: - "))
print(num2)
last_number = int(repr(num2)[-1])
print(f"The last number of {num2} is {last_number}.")

# Program to check whether the last digit of number is divisible by 7 or not
num3 = int(input("Enter number: - "))
print(num3)
last_number = int(repr(num3)[-1])% 7 == 0
print(f"The last number of {num3} is {last_number}.")
if num3 % 7 == 0 and num3 != 0:
    print("Divisible by 7.")
else:
    print("Not Divisible by 7")

# Program to check whether a year is leap year or not
year = int(input("Enter year: - "))
print(year)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year.")

# Program to accept a number from 1 to 7 and display the name of day like 1 for Sunday, 7 for Saturday
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
