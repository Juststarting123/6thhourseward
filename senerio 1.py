#name: Seeley Seward
#class: hour 6
#Assignment: scenario 1

enemydict={
    "enemy1":{
        "name" : "spider king",
        "type" : "boss enemy",
        "magic abilities" : False,
        "damage" :10,
    }, "enemy2":{
        "name": "mushroom man",
        "type": "boss enemy",
        "magic abilities": False,
        "damage": 20,
    },
    "enemy3":{
        "name": "shadow creature",
        "type": "rare enemy",
        "magic abilities": True,
        "damage": 11,
    },
    "enemy4":{
        "name": "bridge troll",
        "type": "common enemy",
        "magic abilities": False,
        "damage": 5,
},
    "enemy5":{
        "name": "regular troll",
        "type": "common enemy",
        "magic abilities": False,
        "damage": 5,
    }
}

enemydict["enemy1"]["damage"]=(int(input("new damage for enemy 1?")))
enemydict["enemy2"]["damage"]=(int(input("new damage for enemy 2?")))
enemydict["enemy3"]["damage"]=(int(input("new damage for enemy 3?")))
enemydict["enemy4"]["damage"]=(int(input("new damage for enemy 4?")))
enemydict["enemy5"]["damage"]=(int(input("new damage for enemy 5?")))
print(enemydict)

print(enemydict["enemy1"]["name"],enemydict["enemy1"]["damage"])
print(enemydict["enemy2"]["name"],enemydict["enemy2"]["damage"])
print(enemydict["enemy3"]["name"],enemydict["enemy3"]["damage"])
print(enemydict["enemy4"]["name"],enemydict["enemy4"]["damage"])
print(enemydict["enemy5"]["name"],enemydict["enemy5"]["damage"])