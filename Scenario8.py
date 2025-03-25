#Name:Seeley seward
#Class: 6th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
class character:
    def __init__( self,health, damage, AC,attack_modifier):
        self.health = health
        self.damage = damage
        self.AC = AC
        self.attack_modifier = attack_modifier

LaeZel = character(12, random.randint(1, 6) + random.randint(1, 6),17,3)
Shadowheart= character(10, random.randint(1, 6), 14, 2)
Gale= character(8, random.randint(1, 10), 14, 0)
Astarion= character(10, random.randint(1, 6), 14, 4)

enemy1 =character(10, random.randint(1, 11) + random.randint(1, 11),14,5)
enemy2 =character(10, random.randint(1, 11) + random.randint(1, 11),14,5)
enemy3 =character(10, random.randint(1, 12) + random.randint(1, 12)+ random.randint(1, 12),14,5)
enemy4 =character(10, random.randint(1, 9),14,5)
enemy5 =character(10, random.randint(1, 8),14,5)







partyAttackRoll = random.randint(1,20) + LaeZel.attack_modifier

if enemy1.AC <  partyAttackRoll:
    enemy1.health -= LaeZel.damage
    print("attack hits,enemy health is",enemy1.health)
    if enemy1.health <=0:
        print("enemy is dead!")
        exit()
    else:
         print("enemy is alive.")
else:
    print("attack misses!")

enemyAttackRoll = random.randint(1,20) + enemy1.attack_modifier

if LaeZel.AC <  enemyAttackRoll:
    LaeZel.health -= enemy1.damage
    print("attack hits,LaeZel health is",LaeZel.health)
    if LaeZel.health <= 0:
        print("LaeZel is dead!")
        exit()
    else:
        print("LaeZel is alive.")
else:
    print("attack misses!")

