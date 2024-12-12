#Name: Seeley Seward Ryan Pool
#Class: 6th Hour
#Assignment: Scenario 5

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).

#The Teams are as such:

#Team 1: Logan B (brain), CJ (hand)
#Team 2: Jax (brain), Colin (hand)
#Team 3: Kyle (brain), Evan (hand)
#Team 4: Ryan (brain), Seeley (hand)
#Team 5: Logan Z (brain), Elijah (hand)


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.




import random
presents =["Toy Car","Teddy bear","Bicycle","Scooter","Baseball bat","Puppy","socks","cloths","coal","Piece of wood","rocks","homework"]
randompresent = []
userresponce = input("is it christmas?")
numpresents = int(input("how many presents do you want?"))
if numpresents >= 13:
    int(input("Too high of number, please retype number of presents."))
elif numpresents <= 0:
    int(input("Too low of number, please retype number of presents."))
presentnumb = random.choice(presents)

presentsum = 0
if userresponce == 'yes':
    for i in (presents):
        presentnumb = random.choice(presents)
        randompresent.append (presentnumb)
    print(randompresent)
elif userresponce == 'no':
    print("ok")


