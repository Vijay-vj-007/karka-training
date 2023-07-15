def add_keychains():
    return("ADD KEYCHAINS")
    


def remove_keychains():
    return("REMOVE KEYCHAINS")
    

def view_order():
    return("VIEW ORDER")
  
    
def checkout():
    return("CHECKOUT")
   

print("\n1. Add keychains to your order\n2. Remove keychains from order\n3. View Current order\n4. Checkout")
choice=int(input("Please enter your choice: "))
if choice == 1:
    print(add_keychains()) 
elif choice == 2:
    print(remove_keychains())
elif choice == 3:
    print(view_order())
elif choice == 4:
    print(checkout())
    exit()
else:
    print ("invalid choice choose between 1 and 4")



        