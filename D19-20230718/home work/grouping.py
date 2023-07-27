items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
]

fruits=[]
vegetable=[]
items={}
for item in items_list:
    if item["category"]=="Fruits":
        fruits.append(item["name"])
    if item["category"]=="Vegetables":
        vegetable.append(item["name"])
# items["Fruits"]=fruits
# items["Vegetables"]=vegetable
items={"Fruits":fruits,"Vegetables":vegetable}
print(items)












