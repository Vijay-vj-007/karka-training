def adventure():
    print("welcome to funny adventure")
    room1=input("you are in a haunted house! you are now in room 1! Would you like to go to room 2 or room 3 ?")


    if room1=="room 2":
        room2=input("would you like to go to room 4 or room 5 ? ")

        if room2=="room 4":
            room4=input("would you like to go to Bed or restroom? ")
            if room4=="bed":
                return" you have reached Bedroom"
            elif room4=="restroom":
                return "you have reached restroom"
            else:
                print("choose between room bed or restroom")
        elif room2=="room 5":
            room5=input("would you like to go to kitchen or upstairs ? ")
            if room5=="kitchen":
                return "you have reached kitchen"
            elif room5=="upstairs":
                return "you have reached upstairs"
            else:
               return "choose between kitchen and upstairs"
        else:
            return "choose between room 4 and room 5"
        
        
    elif room1=="room 3":
        room3=input("would you like to go to room 6 or room 7 ? ")
        if room3=="room 6":
            room6=input("would you like to go to pool or bar")
            if room6=="pool":
                 return  " you have reached pool"
            elif room6=="bar":
                 return "you have reached bar"
                
            else:
                return"choose between room pool or bar"
            
       
        if room3=="room 7":
            room7=input("would you like to go to theatre or exit")
            if room7=="theatre":
                return "you have reached theatre"
            elif room7=="exit":
                return "you have reached exit door of house"
            else:
                return "choose between kitchen and upstairs"
    else:
        return "choose betweem room 2 and room 3"

print(adventure())

