



#area of triangle

def area_of_triangle():
        
        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))
        c = float(input('Enter third side: '))

        s = (a + b + c) / 2.

        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return f"area of the triangle, {area}"

    

    #area of square

def area_of_square():
    
        side=float(input("enter the side : "))
        area=side * side
        return f"area of square,{area} "


    #area of rectangle

def area_of_rectangle():

        length=float(input("Enter the value of length : "))
        width=float(input("Enter the value of width : "))

        area=width * length
        return f"area of rectangle,{area}"

   

    #area of circle

def area_of_circle():

        radius=float(input("Enter the radius of the circle : "))
        area=3.14 * (radius*radius)
        return f"area of circle,{area}"


   
    #area of   trapezium

def area_of_trapezium():

        base_1=float(input("Enter the base 1: "))
        base_2=float(input("Enter the base 2: "))
        height=float(input("Enter the height: "))

        area=(base_1+base_2)/2 * height
        return f"area of trapezium,{area}"

    


print("\n1) Area of triangle\n2) Area of square\n3) Area of rectangle\n4) Area of Circle\n5) Area of trapezium") 

choose=int(input("Enter the choice: "))

if choose==1:
    print(area_of_triangle())
elif choose==2:
    print(area_of_square())
elif choose==3:
    print(area_of_rectangle())
elif choose==4:
        print(area_of_circle())
elif choose==5:
     print(area_of_trapezium())  




