from difflib import Match

Roll = input("Enter Roll No.: -")
Name = input("Enter Name: -")
English = int(input("Enter Obtain Mark: -"))
Math = int(input("Enter Obtain Mark: -"))

#Mark Sheets
Total = English+Math
Average = int(English+Math)/2
print("Total Obtained Marks: -", Total)

#Result
if English < 40 or Math < 40:
    print("Result: Failed")
else:
    print("Result: Passed")

#Remark
print("Average Marks: - ", Average)
if Average < 40 or English < 40 or Math < 40:
    print("Remark: Failed")
elif Average < 60:
    print("Remark: Second")
elif Average < 80:
    print("Remark: First")
elif Average < 100:
    print("Remark: Distinction")