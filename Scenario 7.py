#Name: Seeley Seward
#Class: 6th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
from Scenario_6 import*
listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(characterlist)/len(characterlist)#Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print(listAverage)