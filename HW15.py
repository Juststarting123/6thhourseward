#Name:Seeley Seward
#Class: 6th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
import random
def hello_world():
    print("Hello World!")


#2. Create a def function that calculates the average of three numbers.

def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print("The average is:", average)


#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animal):
    print("The 3rd animal's name is", animal[2])

#4. Create a def function that loops from 1 to the number put in the argument.
def number_count(x):
    for i in range(1,x+1):
        print(i)

#5. Call all of the functions created in 1 - 4 with relevant arguments.

hello_world()
calculate_average(5, 10, 15)
animal_list("Roy", "Steven", "James","billy","Tom")
number_count(12)


