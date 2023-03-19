string = input()
result = 0

for s in string:
    result = max(result + int(s), result * int(s))

print(result)