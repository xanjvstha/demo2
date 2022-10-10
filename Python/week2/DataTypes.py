#None
from array import array
import sys
#int - 123
#None - None
#float - 123.456
#bool - True/False
#complex - 1234+567j
#ARRAY -('i', []) - int & float
#LIST - []
#TUPLE - ()
#SET - {}

var1 = [1,2,3,1,2,6,7] #list - list can have duplicate
var2 = set(var1) # set - set only provides unique and no duplicate value
print(var1)
print(var2)
del var1
del  var2

# var1 = 123.555 # 16 bits (16 digits only)
# var1 = True
# var1 = (3,4,5,6,7,8,9,1,2,3,4,5,6,7,8)
# var1 = {'sid':13123, 'name':'Sanjeev'}
# print(var1) #accessing value
# print(type(var1))
# print(id(var1))
# print(sys.getsizeof(var1))
# print(len(var1))
# print(max(var1))
# print(min(var1))
# print(sum(var1))