#name: Seeley Seward
#class: 6th hour
#assignment:scenario 2

partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}

enemydict={ "enemy2":{
    "name": "mushroom man",
        "type": "boss enemy",
        "magic abilities": False,
        "damage": 20,
        "health": 30,
        "ac":50
     }
    }
y = partyDictionary["LaeZel"]["Damage"]
x = enemydict["enemy2"]["health"]
z = x - y
print(z)
