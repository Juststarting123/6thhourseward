#Name:Seeley Seward
#Class: 6th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.

try:
    print(x)
except:
    print("Hello World!")
#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.

try:
    y = int(input("enter number here."))
    print(100/y)
except ZeroDivisionError:
    print("you cannot divide by 0")



#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    z = int(input("enter a number here."))
    print(z)
except ValueError:
    print("Letters are not valid.")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
j=5
while j>=0:
    print(j)
    j-=1
    if j<0:
        raise Exception("No number can be below zero.")