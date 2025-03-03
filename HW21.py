#Name:
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sportdict = {
    "sport1":{
     "sport":"baseball",
    "people": 26,
    "ball": True

    },
    "sport2":{
      "sport2":"basketball",
        "people":10,
        "ball": True
    },
    "sport3":{
    "sport":"football",
    "people":22,
    "ball": True
    }
}




#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def sportthing(x,y,z):
    print(x + y + z)
#3. Call the function with arguments here


sportthing(sportdict["sport1"]["people"],sportdict["sport2"]["people"],sportdict["sport3"]["people"])