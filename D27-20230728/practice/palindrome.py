a = "level"
start = 0
end = len(a) - 1
while start <= end:
    if a[start] != a[end]:
        print("The string is not a palindrome.")
        break
    start += 1
    end -= 1
else:
    print("The string is a palindrome.")
