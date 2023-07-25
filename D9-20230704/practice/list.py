
"""names_set={"vijay","abisheak","ajith","shalini","vinusha","gayathiri"}
print (names_set[0])"""


"""name="vijay"
my=name[0:4]
print(my)
"""


"""names=["vijay","abisheak","ajith","shalini","vinusha","gayathiri"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])"""


"""names=["vijay","abisheak","ajith","shalini","vinusha","gayathiri"]
for name in names:
    print(name)"""


"""names=["vijay","abisheak","ajith","shalini","vinusha","gayathiri"]
for name in names:
    upper=(name.upper())
    print(upper)"""


"""names=["vijay","abisheak","ajith","shalini","vinusha","gayathiri"]
for name in names:
    print(name.upper())
    print(name.capitalize())
    print("my name is ",name.capitalize())
 """



# names=["vijay","abisheak","ajith","shalini","vinusha","gayathiri"]
# for i,name in enumerate(names):
#     if i< 4:
#         print(i,name)




fruits=["apple","strawberry","mango","litchie","grapes"]
for i,fruit in enumerate(fruits):
    if i<=2:
        print(fruit)
    else:
        break
