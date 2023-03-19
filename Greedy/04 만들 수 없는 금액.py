n = int(input())
numbers = list(map(int, input()))
numbers.sort()

target = 1
for i in range(n):
    if numbers[i] > target:
        break
    target += numbers[i]

print(target)