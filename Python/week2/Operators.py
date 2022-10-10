import math
from array import array

# int - 123
# None - None
# float - 123.456
# bool - True/False
# complex - 1234+567j int + string
# ARRAY - var2 = array('i', [2]) - int & float
# LIST - [2,3,4], [23], ["sanjeev"]
# TUPLE - ()
# SET - {}
# DICT - {'id':1, "name":"Sanjeev"}
# Assignment Operator
# = simple assignment operator
# shift value from right to left variables
# var1 = 20
# print(var1)
#
# var1, var2 = 34, 45
# print(var1, var2)
#
# var1, var2 = var2, var1
# print(var1, var2)
#
# # Multiple Assignment
# var1 = var2 = var3 = 100
# print(var1, var2, var3)
# print(id(var1))
# print(id(var2))
# print(id(var3))
#
# # short-hand assignment operator
# num1 = 20
# # num1 = num1 + 5
# num1 += 5
# print(id(num1))
# print(num1)
#
# 2. Arithmetic Operators
# Class - User defined type
# int - 123
# float - 123.11
# str-name
# list - [123]
# tuple -(132)
#
# n1 = array('i', [3, 4, 5])
# n2 = array('i', [6, 7, 8])
# n3 = n1 + n2
# print(n3)

# class C1:
#     pass
#
# object1 = C1()
# print(type(object1))
# print(id(object1))
# print(object1)
#
# None
# var1 = None
# var2 = None
# var3 = var1 + var2
# print(var3)

# Bool
# var1 = True
# var2 = False
# var3 = var1 + var2
# print(var3)

# Integer
# var1 = 20
# var2 = 7
# var3 = var1 + var2
# print(var3)
#
# var1 = 20
# var2 = 70
# var3 = var1 - var2
# print(var3)
#
# var1 = 20
# var2 = 7
# var3 = var1 * var2
# print(var3)
#
# var1 = 20
# var2 = 7
# var3 = var1 / var2
# print(var3)

# var1 = 20
# var2 = 7
# var3 = var1 // var2
# var4 = var1 % var2
# var5 = var1 ** var2
# print(var4)
# var6 = math.pow(3, 4)
# print(var6)
# var7 = math.sqrt(49)
# print(var7)

# 3. Relational Operator
# Compare two value and return boolean result
# == Equals to
# value1 is equals to value2 -> True
# var1 = {"id":1, "name":"Sanjeev"}
# var2 = {"id":1, "name":"Sanjev"}
# var1 = array('i', [2])
# var2 = array('i', [2])
# result = (var1 == var2)
# print(result)

# Greater Than
# Left value is greater than right value
# num1 = 88
# num2 = 80
# result = num1 > num2
# print(result)

# Lesser Than
# Left value is greater than right value
# num1 = 88
# num2 = 89
# result = num1 < num2
# print(result)

# Greater Than or Equals to
# Left value is greater than right value or equals to right value->True
# num1 = 10
# num2 = 10
# result = num1 >= num2
# print(result)

# Lesser Than or Equals to
# Left value is greater than right value or equals to right value->True
# num1 = 15
# num2 = 15
# result = num1 <= num2
# print(result)

# Not equal to !=
# Left value is not equals to right value
# num1 = 15
# num2 = 15
# result = num1 == num2
# result1 = num1 != num2
# print(result, result1)

# 4. Logical Operator
# a. and
# result = (10>5) and (10>6)
# print(result)
# result = (10>50) and (10>6)
# print(result)

# b. or
# result = (10>5) or (10>6)
# print(result)
# result = (10>50) or (10>6)
# print(result)

# c. not
# True -> False
# False -> True
print(not True)
print(not False)
print(not True or True)
print(not False and False)

# 5. Other Operators
# [], {}, (), .
