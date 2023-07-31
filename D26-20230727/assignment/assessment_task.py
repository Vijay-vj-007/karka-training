num = [1, 0, 4, 5, 0, 6, 7, 0]
output = []
length=len(num)
for i in num:
    if i == 0:
        output += [i, 0]
    else:
        output.append(i)

print(output[:length])
