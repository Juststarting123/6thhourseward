#Name: Seeley Seward
#Class: 6th Hour
#Assignment: HW6
#Objectives

#1. Print Hello World!

#2. Create a variable named num and assign it a number.

#3. Create a nested if statement follows this structure:

#If num is divisible by 2
#   if num is divisible by 3
#       print the result of num being divided by 2
#       print the result of num being divided by 3
#   else
#       print that it is not divisible by 3
#       print the result of num being divided by 2
#else
#   if num is divisible by 3
#       print that num is not divisible by 2
#       print the result of num being divided by 3
#   else
#       print that neither is divisible by 2 or 3
print("hello world")

num=6
if num % 2==0:
    if num % 3==0:
        print("num is divisible by 2")
        print("num is divisible by 3")
    else:
        print("num is not divisible by 3")
        print("num is divisible by 2")
else:
    if num % 3==0:
        print("num is not divisible by 2")
        print("num is divisible by 3")
    else:
        print("neither is divisible by 2 or 3")