def male_or_female():
    gender=input("Enter your gender? ")
    first_name=input("Enter your first name? ")
    last_name=input("Enter your last name? ")
    age=int(input("Enter your age? "))
    if gender == "female":
        if age >=20:
            marital_status=input(f"Are you married, {first_name} (y or n) ")
            if marital_status == "y":
                print(f"Then i shall call you Mrs.{last_name}")
            else:
                print(f"Then i shall call you Ms.{last_name}")
        else:
            print(f"Then i shall call you {first_name} {last_name}")

    elif gender == "male":
        if age >=20:
            print(f"Then i shall call you Mr.{first_name} {last_name}")
        else:
            print(f"Then i shall call you {first_name} {last_name}")
    else:
        print("invalid gender choose male or female")

male_or_female()


