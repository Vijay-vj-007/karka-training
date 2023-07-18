names=[{"name":"vijay",
        "place":"marthandam",
        "hobbies":["listening music","watching movies","cricket"],
        "SSLC":{"TAMIL":80,"ENGLISH":90,"MATHS":70,"SCIENCE":90,"SOCIAL":88}},
       {"name":"abisheak",
        "place":"kotar",
        "hobbies":["listening music","browsing","watching movies"],
        "SSLC":{"TAMIL":90,"ENGLISH":90,"MATHS":80,"SCIENCE":70,"SOCIAL":78}},
       {"name":"shalini",
        "place":"vadasery",
        "hobbies":["chatting with friends","drawing","listening music"],
        "SSLC":{"TAMIL":76,"ENGLISH":85,"MATHS":90,"SCIENCE":70,"SOCIAL":68}},
       {"name":"siva gayathiri"
        ,"place":"kotar"
        ,"hobbies":["watching movies","listening movies","dance"],
        "SSLC":{"TAMIL":100,"ENGLISH":78,"MATHS":83,"SCIENCE":67,"SOCIAL":88}},
       {"name":"vinusha",
        "place":"eethamozhi",
        "hobbies":["listening music","watching movies","playing"],
        "SSLC":{"TAMIL":99,"ENGLISH":97,"MATHS":85,"SCIENCE":100,"SOCIAL":98}}]

def detail(names):
    total=0

    for name in names:
        tamil=name["SSLC"]["TAMIL"]
        english=name["SSLC"]["ENGLISH"]
        maths=name["SSLC"]["MATHS"]
        science=name["SSLC"]["SCIENCE"]
        social=name["SSLC"]["SOCIAL"]
        total=tamil+english+maths+science+social
        print("TOTAL is: ",total)
        percentage=(total/500)*100
        print("Percentage is: ",percentage)

        if percentage > 90 or (percentage > 75 and maths > 98):
            print("You are eligible for MATHS BIOLOGY")
        elif (percentage >80 and percentage <90 ) or (percentage > 70 and maths > 90):
            print("You are eligible for COMPUTER SCIENCE")
        else:
            print("Please choose other categories")

detail(names)