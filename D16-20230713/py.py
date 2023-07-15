number=int(input("enter the number: "))
def function(number):
    num = ""
    for i in range(1, number+1):
        if i % 2 == 0:
            num=num+ "*"
        num=num+i
        print(num)
function(number)
