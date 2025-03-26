#Name:Seeley Seward
#Class: 6th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class dnd:
    def __init__(self, health, damage, speed,max_health):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health

    def damage_loop(self):
        for i in range(1, 11):
            self.health -= random.randint(1, 6)
            print(self.health)
            time.sleep(1)

    def healing_potion(self):
        self.health += (30)
        if self.health > 100:
            self.health = 100
        print(self.health)
#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
Steve = dnd(100, 20, 30,100)
Alex = dnd(60, 10, 30,60)
villager =dnd(50, 30, 40,50)
baby_villager =dnd(45, 35, 25,45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
d4=random.randint(1, 4)
if d4 ==1:
    Steve.damage_loop()
elif d4 ==2:
    Alex.damage_loop()
elif d4 ==3:
    villager.damage_loop()
elif d4 ==4:
    baby_villager.damage_loop()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
if Steve.health < Steve.max_health :
    Steve.healing_potion()
elif Alex.health < Alex.max_health :
    Alex.healing_potion()
elif villager.health < villager.max_health :
    villager.healing_potion()
elif baby_villager.health < baby_villager.max_health :
    baby_villager.healing_potion()
