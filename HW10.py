#Name:
#Class: 6th Hour
#Assignment: HW10
import time

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    time.sleep(1)
    i -= 1
else:
     print("Hello world")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
o = 1
while o<=30:
    if o % 2 == 0:
        print(o)
    o+=1


#3. Create a while loop that repeats until the user
#inputs the number 0.
p = int(input("Enter a integer:"))
while p  !=0:
    print(p)
    p = int(input("Enter a integer:"))








