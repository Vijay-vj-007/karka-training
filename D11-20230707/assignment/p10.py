name=input("What's your name ? ")
age=int(input(f"ok, {name}, how old are you ? "))

if age < 16:
    print(f"you can't drive,vote,rent a car, {name}")
if age >= 16 and age <= 17 :
    print(f"yoy can drive but you can't vote, {name}")
if age >=18 and age <=24:
    print(f"you can drive and vote but you can't rent a car, {name}")
if age >=25:
    print(f"you can do pretty much anything, {name}")
    
