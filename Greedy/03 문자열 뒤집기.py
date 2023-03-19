string = input()
temp = string[0]
count = 0
for s in string:
    if s != temp:
        count += 1
        temp = s

print(count-1)