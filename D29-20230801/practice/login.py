def user_list():
    users = [{
        "Name": "Vijay",
        "Email": "vijay@gmail.com",
        "Password": "vijay123",
        "Hobbies": ["playing cricket", "listening music"],
        "Friend List": ["ajith", "surya"],
    },{
        "Name": "ajith",
        "Email": "ajith@gmail.com",
        "Password": "ajith123",
        "Hobbies": ["acting", "music"],
        "Friend List": ["vijay", "surya"],
    },{
        "Name": "surya",
        "Email": "surya@gmail.com",
        "Password": "surya123",
        "Hobbies": ["dancing", "music"],
        "Friend List": ["ajith", "vijay"],
    }]
    return users

email = input("Enter the email: ")
password = input("Enter the password: ")


def user_details(email,password):
    users = user_list()
    for user in users:
        if user["Email"] == email and user["Password"] == password:
            user["loggedin"] = True
            return user


user = user_details(email,password)
def display_details(user):
    details=""
    if user:
        details += f"{user['Name']} | {user['Email']}\n"
        details += f"Your hobbies are: {user['Hobbies']}\n"
        details += f"Your friend list: {user['Friend List']}"
        return details
    else:
        return "Invalid email or password."

output=display_details(user)
print(output)

