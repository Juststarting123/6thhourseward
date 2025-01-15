#Name:Seeley Seward
#class:6th hour
#Assignment:HW16
import random
from timeit import repeat


#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

def rock_paper_scissors():
    rock =1
    paper =2
    scissors=3
    playernum = int(input("Choose 1 for rock,2 for paper,or 3 for scissors"))
    opponentnum= random.randint(1,3)

    if playernum ==1 and opponentnum ==3:
        print("You win!")
    elif playernum==1 and opponentnum==2:
        print("You lose!")
    elif playernum==1 and opponentnum==1:
        print("Tie!")
    if playernum == 2 and opponentnum == 1:
        print("You win!")
    elif playernum == 2 and opponentnum == 3:
        print("You lose!")
    elif playernum ==2 and opponentnum == 2:
        print("Tie!")
    if playernum == 3 and opponentnum == 2:
        print("You win!")
    elif playernum == 3 and opponentnum == 1:
        print("You lose!")
    elif playernum == 3 and opponentnum == 3:
        print("Tie!")

    game_repeat()


def game_repeat():
    repeatInput = input("Would you like to try again?")
    if repeatInput == "y":
        rock_paper_scissors()
    else:
        exit()
rock_paper_scissors()

