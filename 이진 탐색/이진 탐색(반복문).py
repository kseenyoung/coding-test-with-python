N, target = list(map(int, input().split()))

numbers = list(map(int, input().split()))
# numbers.sort()

start, end = 0, len(numbers)-1
idx = end//2

while start != end:
    if numbers[idx] == target:
        print(idx+1)
        exit()
    elif numbers[idx] < target:
        start = idx + 1
        idx = (end-start)//2 + start
    else:
        end = idx - 1
        idx = (end - start) // 2 + start
if numbers[start] == target:
    print(numbers[start])
else:
    print("원소가 존재하지 않습니다.")
