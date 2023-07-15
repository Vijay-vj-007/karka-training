print("Ye Olde keychain shoppee")

your_cart=0
sales_tax=8.25
shipping_cost=5.00
shipping_cost_per_keychain=1.00

def add_keychains(your_cart):
    print("ADD KEYCHAINS")
    add=int(input("You have 0 keychains. How many to add? "))
    if add<0:
        return"you must select atleast one keychain"

    your_cart=your_cart+add
    print( f"you have {your_cart} keychains")
    return your_cart



def remove_keychains(your_cart):
    print("REMOVE KEYCHAINS")
    remove=int(input(f"You have {your_cart} keychains. How many to remove? "))
    your_cart=your_cart-remove
    if your_cart < 0:
        return"you cant remove less than 0"
        
    print(f"you have now {your_cart} keychains" )
    return your_cart

def view_order(your_cart,shipping_cost,sales_tax,shipping_cost_per_keychain):
    print("VIEW ORDER")
    subtotal=your_cart*10
    shipping_charges=shipping_cost+(your_cart*shipping_cost_per_keychain)
    tax=(subtotal*sales_tax)/100
    total_cost=subtotal+shipping_charges+tax
    print( f"you have {your_cart} keychains.\nKeychains costs $10 per each.\nShipping Charges  {shipping_charges}.\nSubtotal  {subtotal}.\nTax  {tax}.\nTotal cost  ${total_cost}.")
    
    return your_cart
  
    
def checkout(your_cart,shipping_cost,sales_tax,shipping_cost_per_keychain):
    print("CHECKOUT")
    name=input("What is your name? ")
    subtotal=your_cart*10
    shipping_charges=shipping_cost+(your_cart*shipping_cost_per_keychain)
    tax=(subtotal*sales_tax)/100
    total_cost=subtotal+shipping_charges+tax
    
    return f"you have {your_cart} keychains.\nKeychains costs $10 per each.\nShipping Charges  {shipping_charges}.\nSubtotal  {subtotal}.\nTax  {tax}.\nTotal cost  ${total_cost}.\nThanks for your order {name}! "


while True:
    print("\n1. Add keychains to your order\n2. Remove keychains from order\n3. View Current order\n4. Checkout")
    choice=int(input("Please enter your choice: "))
    if choice == 1:
        your_cart = (add_keychains(your_cart)) 
    elif choice == 2:
        your_cart = (remove_keychains(your_cart))
    elif choice == 3:
        print(view_order(your_cart,shipping_cost,sales_tax,shipping_cost_per_keychain))
    elif choice == 4:
        print(checkout(your_cart,shipping_cost,sales_tax,shipping_cost_per_keychain))
        break
    else:
        print ("invalid choice choose between 1 and 4")
