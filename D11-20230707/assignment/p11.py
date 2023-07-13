weight_on_earth=float(input("Enter the weight in earth : "))

print("\nI have informations for the following planets:")

print("\n1.Venus\t\t2.Mars\t\t3.Jupiter\n4.Saturn\t5.Uranus\t6.Neptune")

planet_choice = int(input("which planet are you visiting ? "))

def relative_gravity(planet_choice):

    if planet_choice == 1:
        gravity = 0.78
        return gravity
    elif planet_choice == 2:
        gravity = 0.39
        return gravity
    elif planet_choice == 3:
        gravity = 2.65
        return gravity
    elif planet_choice == 4:
        gravity = 1.17
        return gravity
    elif planet_choice == 5:
        gravity = 1.05
        return gravity
    elif planet_choice == 6:
        gravity = 1.23
        return gravity
    else:
        choice="Invalid planet choice!"
        return choice

result=relative_gravity(planet_choice)
destination_weight = weight_on_earth * result

print(f"Your weight would be {destination_weight} pounds on that planet")


