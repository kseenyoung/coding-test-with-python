n, m = map(int, input().split())
alist = list(map(int, input().split()))

# 방법1
result = 0

for i in range(n):
    for j in range(i+1, n):
        if alist[i] != alist[j]:
            result += 1

print(result)

# 방법 2
numbers = [0]*11
for i in range(n):
    numbers[alist[i]] += 1
answer = 0
for i in range(1, m+1):
    n -= numbers[i]
    answer += numbers[i]*n

print(answer)