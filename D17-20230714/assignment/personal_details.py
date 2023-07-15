personal_details=[{"name":"vijay","age":23,"place":"marthandam"},
                  {"name":"abisheak","age":22,"place":"kotar"},
                  {"name":"shalini","age":22,"place":"vadasery"},
                  {"name":"siva gayathiri","age":21,"place":"kotar"},
                  {"name":"vinusha","age":21,"place":"eethamozhi"}]

def person_detail(personal_details):
    for person in personal_details:

        name=person["name"]
        age=person["age"]
        place=person["place"]
        print(f"I am {name},I am {age} years old,and i am from {place} .")
person_detail(personal_details)
        
def age_above(personal_details):
    print("\nperson above age 21\n")
    for person in personal_details:
        name=person["name"]
        place=person["place"]
        if person["age"] > 21:
             print(f"Name:{name}\nPlace:{place}\n")
age_above(personal_details)


    