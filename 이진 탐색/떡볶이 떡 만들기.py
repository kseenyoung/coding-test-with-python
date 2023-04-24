# 내 코드
# import numpy as np

# N, M = list(map(int, input().split()))
# numbers = np.array(list(map(int, input().split())))
#
# result = max(numbers)-1
# maxM = np.array([-result]*N)
# maxM = sum([i for i in np.add(numbers, maxM) if i > 0])
#
# while maxM < M:
#     result -= 1
#     maxM = np.array([-result] * N)
#     maxM = sum([i for i in np.add(numbers, maxM) if i > 0])
#
# print(result)


# 결과 코드
N, M = list(map(int, input().split()))
numbers = list(map(int, input().split()))

start, end = 0, max(numbers)

while end >= start:
    total = 0
    mid = (start+end)//2
    for x in numbers:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
