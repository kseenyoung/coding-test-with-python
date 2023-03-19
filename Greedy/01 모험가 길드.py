n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

result = 0
temp = 0
for i in range(n):
    temp += 1
    if temp >= numbers[i]:
        result += 1
        temp = 0

print(result)