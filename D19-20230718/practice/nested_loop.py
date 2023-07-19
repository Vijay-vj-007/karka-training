educational_qualification=[{"Study":"B.E",
                            "institute":"Mar ephraem college of engineering and technology",
                            "semester_marks":[{"semester_name":1,
                                               "subjects":["Computer","maths_1","chemistry"],
                                               "semester_grade":"A",},
                                               {"semester_name":2,
                                               "subjects":["thermal_1","maths_3","fluid mech"],
                                               "semester_grade":"B",},
                                               {"semester_name":3,
                                               "subjects":["thermal_2","maths_3","BEEE"],
                                               "semester_grade":"A",}]
                            }]

for item in educational_qualification:
    print(item["Study"])
    marks=item["semester_marks"]
    for sem in marks:
        print(sem["semester_grade"])
