# Result Processing
# declare
sid = None
fullname = None
English = None # Obtained Mark
Math = None
Science = None
Social = None
# input
sid = input("Enter Student ID: ")
fullname = input("Enter Full Name: ")
English = int(input("Enter English Mark:"))
Math = int(input("Enter Math Mark:"))
Science = int(input("Enter Science Mark:"))
Social = int(input("Enter Social Mark:"))
# process
# calculate total
Total = English + Math + Science + Social

# calculate average
Average = Total / 4


# calculate result
Result = (English >= 40 and Math >= 40 and Science >= 40 and Social >= 40)


# Output
print("SID : {}".format(sid))
print("Full Name: {}".format(fullname))
print("English: {}".format(English))
print("Math: {}".format(Math))
print("Science: {}".format(Science))
print("Social: {}".format(Social))
print("Total: {}".format(Total))
print("Average: {}".format(Average))
print("Result: {}".format(Result))