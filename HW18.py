#Name: Seeley Seward
#Class: 6th Hour
#Assignment: HW18
import random

#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello_world():
    print("Hello World!")
hello_world()
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
Beanbag_list=["red","blue","green","yellow","purple"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def Beanbag_choosing():
    if not Beanbag_list:
        print("The bag is empty")
    else:
        chooser=random.choice(Beanbag_list)
        print(chooser)
        Beanbag_list.remove(chooser)
        game_repeat()

#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def game_repeat():
    repeatInput = input("Would you like to try again?")
    if repeatInput == "y":
        Beanbag_choosing()
    else:
        exit()

#5. Call the #3 function at the bottom.
Beanbag_choosing()
