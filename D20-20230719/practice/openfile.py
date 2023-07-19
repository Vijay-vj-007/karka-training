# read file

# file=open("/home/vijay/txt/karka.txt","r")
# for line in file:
#     print(line)


# data=file.read()
# print(data)

# write file

# file=open("/home/vijay/txt/karka.txt","w")
# file.write("I am mechanical engineer\ncurrently i studying in karka")
# file.close()


# file=open("/home/vijay/txt/karka.txt","r")
# print(file.read())

#to write with out erasing the old data
file=open("/home/vijay/txt/karka.txt","a")
file.write("\nMy name is vijay\nI am 23 years old")
file.close()

file=open("/home/vijay/txt/karka.txt","r")
# print(file.read())
for line in file:
    print(line.split())