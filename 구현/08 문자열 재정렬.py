string = input()

result = ''
num = 0
for s in string:
    if s.isdigit():
        num += int(s)
    else:
        result += s

result = sorted(result, key=lambda x: x)
print(''.join(result) + str(num))
