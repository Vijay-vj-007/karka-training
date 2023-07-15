
def quizz():
   
    overall=0
    quiz=input("Are you ready for quiz ? (Y or N)")

    if quiz == "Y":
        print("Okay! here it comes")
    if quiz == "N":
        return "thank you"
    
    q1=input("Q1) What is the capital of Alaska?\n1) Melbourne\n2) Anchorage\n3) Juneau\n> ")
    
    if q1 == "3":
        print ("That's right!")
        overall=overall+1
    else:
        print(f"{q1},is not capital of alaska")

    q2=input("Q2) Can you store the value \"CAT\" in a variable of type int?\n1) Yes\n2) No\n> ")
    
    if q2 == "2":
        print ("That's right")
        overall=overall+1
    else:
        print("sorry, \"CAT\" is a string.\nint can only store numbers")
    
    q3=input("Q3) what is result of 9+6/3?\n1) 5\n2) 11\n3) 15/3\n> ")
    
    if q3 == "2":
        print ("That's correct")
        overall=overall+1
    else:
        print(f"sorry,{q3} is not the correct answer ")
    return (f"Overall, you got {overall} out of 3 correct.\nThanks for playing!")    

print(quizz())


