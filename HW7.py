#Name:
#Class: 6th Hour
#Assignment: HW7
from operator import truediv

print("hello world")

#1. Print Hello World!
#2. Create three different boolean variables named wifi, login, and admin.
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

wifi=True
login=True
Admin=True
Login_count=0
#make if statement to see if true
if wifi == True:
    if login == True:
        if Admin == True:
            print("welcome!")
            Login_count += 1
            print(Login_count)
        else:
            print("unauthorized account")
    else:
        print("incorrect login")
else:
    print("No wifi")