# Digital Clock
import datetime
import time

while True:
    time.sleep(1)
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")
    print("Date: -", date)
    print("Time", now)
    break

# Multiplication Table
table = int(input("Display multiplication table of:-"))
print("The multiplication Table of:-", table)
while table <= 10:
    count = 1
    while count <= table:
        result = table * count
        print(table,'*',count, '=', result)
        count = count + 1
    table = table + 1

