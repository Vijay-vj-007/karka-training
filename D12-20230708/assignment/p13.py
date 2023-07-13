
def guess():

    print("TWO MORE QUESTIONS!")
    print("Think of an object, and i will try to guess it.")

    question1= input("Is it animal, vegetable, or mineral?")
    
    if question1 == "animal":
       
        question2=input("Is it bigger than a breadbox?")
        
        if question2 == "yes":
            print("my guess is that you are thinking of a mouse\nI would ask you if am right, but i dont actually care.")
        elif question2 =="no":
            print("my guess is that you are thinking of a squirrel\nI would ask you if am right, but i dont actually care.")
        else:
            print("no such command found use only yes or no")
    
    elif question1 == "vegetable":
        
        question2=input("Is it bigger than a breadbox?")
        
        if question2 == "yes":
            print("my guess is that you are thinking of a Watermelon\nI would ask you if am right, but i dont actually care.")
        elif question2 =="no":
            print("my guess is that you are thinking of a Carrot\nI would ask you if am right, but i dont actually care.")
        else:
            print("no such command found use only yes or no")

    
    elif question1 == "mineral":
        
        question2=input("Is it bigger than a breadbox?")
        
        if question2 == "yes":
            print("my guess is that you are thinking of a Camaro\nI would ask you if am right, but i dont actually care.")
        elif question2 =="no":
            print("my guess is that you are thinking of a Paper clip\nI would ask you if am right, but i dont actually care.")
        else:
            print("no such command found use only yes or no")
    
    else:
        print("Invalid answer. (Please choose \"animal\", \"vegetable\", or \"mineral\"")
    
guess()
