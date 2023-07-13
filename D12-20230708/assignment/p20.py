def sum():
    sum=0
    
    while True:
        number=int(input("Enter the number (enter 0 to stop): "))
        
        if number ==0:
            break

        sum = sum+number
        
        print (f"your number so far: {sum}")
    print("The sum of given numbers is : ",sum)

sum()
    
    
