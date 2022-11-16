import random 
classmate = ["seabs", "alex", "dami", "brandon", "jacob", "ricky", "chocoflan", "mando", "jordy", "gonzo"]
locations = ["cafeteria", "park", "room 110", "backroom", "hallway"]

def Clue():
    person2 = random.randrange(0, 9)
    location = random.randrange(0, 4)
    person1 = random.randrange(0, 9)
    prank = random.randrange(0, 100)
    
    if prank < 10:
        print(classmate[person2], "got merked by a water ballon in", locations[location], "by", classmate[person1])
    elif prank < 30:
        print(classmate[person2], "got pied at", locations[location], "by", classmate[person1])
    elif prank < 65:
        print(classmate[person2], "recieved choco chipi cookie but it was actually oatmeal raisin at", location[location], "by", classmate[person1])
    elif prank < 80:
        print(classmate[person2], "got they shoelaces tied together in", location[location], "by", classmate[person1])
    else:
        print(classmate[person2], "got turned into a lil itty bitty wabit in", location[location], "by", classmate[person1])
        


Clue()

#i = 0
#while i <= 10:
    #Clue()
    #print()
    #i += 1

#its bugged idk whats wrong with it. it only happens when i try to call the function 
