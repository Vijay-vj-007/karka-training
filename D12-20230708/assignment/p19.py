import random

def game():
    number=random.randint(1,100)
    tries=0

    while tries < 7:
        guess=int(input("Enter the number: "))
        tries=tries+1

        if guess > number:
            print("Too High")
        elif guess < number:
            print("Too Low")
        else:
            print("Congratulations! You have guessed the correct number!")
            return
    print("Sorry, you have reached the maximum number of tries.")
    print("The number was: ",number)
game()
