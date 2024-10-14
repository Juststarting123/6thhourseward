#Name: Seeley Seward
#Class: 6th Hour
#Assignment: Scenario 3

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4
import random




#Party Dictionary Goes Here
partyDictionary = {
    "LaeZel" : {

        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" :10,
        "Damage roll":random.randint(1,6)+random.randint(1,6),
        "attack modifier":3,


    },
    "Shadowheart" : {

        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
        "Damage roll":random.randint(1,6),
        "attack modifier":2,
    },
    "Gale" : {

        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
        "Damage roll":random.randint(1,10),
        "attack modifier":0,
    },
    "Astarion" : {

        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
        "Damage roll":random.randint(1,6),
        "attack modifier":4,
    }
}


#Enemy Dictionary Goes Here
enemydict={
    "enemy1":{
        "name" : "spider king",
        "type" : "boss enemy",
        "magic abilities" : False,
        "Damage" :10,
        "AC" : 14,
        "Damage roll":4,
        "attack modifier":5,
        "Health":10,
    }, "enemy2":{
        "name": "mushroom man",
        "type": "boss enemy",
        "magic abilities": False,
        "Damage": 20,
        "AC" : 14,
        "Damage roll":random.randint(2,11),
        "attack modifier":5,
        "Health":10,
    },
    "enemy3":{
        "name": "shadow creature",
        "type": "rare enemy",
        "magic abilities": True,
        "Damage": 11,
        "AC" : 14,
        "Damage roll":random.randint(3,12),
        "attack modifier":5,
        "Health":10,
    },
    "enemy4":{
        "name": "bridge troll",
        "type": "common enemy",
        "magic abilities": False,
        "Damage": 5,
        "AC" : 14,
        "Damage roll":random.randint(1,9),
        "attack modifier":5,
        "Health":10,
    },
    "enemy5":{
        "name": "regular troll",
        "type": "common enemy",
        "magic abilities": False,
        "Damage": 5,
        "AC" : 14,
        "Damage roll":random.randint(1,8),
        "attack modifier":5,
        "Health":10,
    }
}

partyAttackRoll = random.randint(1,20) + partyDictionary["LaeZel"]["attack modifier"]

if enemydict["enemy1"]["AC"] <  partyAttackRoll:
    enemydict["enemy1"]["Health"] -= partyDictionary["LaeZel"]["Damage roll"]
    print("attack hits,enemy health is",enemydict["enemy1"]["Health"])
    if enemydict["enemy1"]["Health"] <=0:
        print("enemy is dead!")
        exit()
    else:
         print("enemy is alive.")
else:
    print("attack misses!")

enemyAttackRoll = random.randint(1,20) + enemydict["enemy1"]["attack modifier"]

if partyDictionary["LaeZel"]["AC"] <  enemyAttackRoll:
    partyDictionary["LaeZel"]["Health"] -= enemydict["enemy1"]["Damage roll"]
    print("attack hits,LaeZel health is",partyDictionary["LaeZel"]["Health"])
    if partyDictionary["LaeZel"]["Health"] <= 0:
        print("LaeZel is dead!")
        exit()
    else:
        print("LaeZel is alive.")
else:
    print("attack misses!")
