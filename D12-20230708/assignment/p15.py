print("TWO MORE QUESTIONS, BABY!")

print("Think of something and i'll try to guess it")

question_1=input("Does it stay inside,outside or both ? ")
question_2=input("Is it a living thing (alive or not alive) ? ")

if question_1 == "inside" and question_2 == "alive":
    print("It is a house plant")
    
if question_1 == "outside" and question_2 == "alive":
     print("It is a bison")

if question_1 == "both" and question_2 == "alive":
    print("It is a dog")

if question_1 == "inside" and question_2 == "not alive":
    print("It is a shower curtain")
    
if question_1 == "outside" and question_2 == "not alive":
     print("It is a billboard")

if question_1 == "both" and question_2 == "not alive":
    print("It is a cellphone")
        
if (question_1 !="inside" and question_1 !="outside" and question_1 !="both") and (question_2 !="alive" and question_2 !="not alive"):
    print("Then what else could you be thinking of besides a python ?!?")


