
#name:Seeley Seward
#class: 6th hour
#Assignment:HM4

print("hello world")

artistdict={
    "name" : "Leonardo da Vinci",
    "art piece" : "Mona lisa",
    "year" : ["1503","1452","1519"]
}

print(artistdict["year"][0])

artistdict.update({"saint jerome in the wilderness":3})
print(artistdict)

artistdict.clear()
print(artistdict)

famouspeople = {
    "person1":{
            "name" : "albert einstein",
    "job" : "theoretical physicist",
    "alive today" : False,
    },
    "person2": {
        "name": "isaac newton",
        "job": " mathematician",
        "alive today": False,
    },
    "person3": {
        "name": "tim berners-lee",
        "job": " English computer scientist",
        "alive today": True,
    }
}
print(famouspeople["person1"]["name"],famouspeople["person2"]["name"],famouspeople["person3"]["name"])
