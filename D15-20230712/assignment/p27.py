print("Ye Olde keychain shoppee")
your_cart=0


def add_keychains(your_cart):
    print("ADD KEYCHAINS")
    add=int(input("You have 0 keychains. How many to add? "))
    your_cart=your_cart+add
    print( f"you have {your_cart} keychains")
    return your_cart


def remove_keychains(your_cart):
    print("REMOVE KEYCHAINS")
    remove=int(input(f"You have {your_cart} keychains. How many to remove? "))
    your_cart=your_cart-remove
    print(f"you have now {your_cart} keychains" )
    return your_cart

def view_order(your_cart):
    print("VIEW ORDER")
    cost=your_cart*10
    print( f"you have {your_cart} keychains.\nKeychains costs $10 per each.\nTotal cost is ${cost}.")
    return your_cart
  
    
def checkout(your_cart):
    print("CHECKOUT")
    cost=your_cart*10
    name=input("What is your name? ")
    return f"You have {your_cart} keychains.\nKeychains cost $10 each.\nTotal cost is ${cost}.\nThanks for your order {name}! "


while True:
    print("\n1. Add keychains to your order\n2. Remove keychains from order\n3. View Current order\n4. Checkout")
    choice=int(input("Please enter your choice: "))
    if choice == 1:
        your_cart = (add_keychains(your_cart)) 
    elif choice == 2:
        your_cart = (remove_keychains(your_cart))
    elif choice == 3:
        print(view_order(your_cart))
    elif choice == 4:
        print(checkout(your_cart))
        break
    else:
        print ("invalid choice choose between 1 and 4")
