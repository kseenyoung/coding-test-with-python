def binarySearch(numbers):
    idx = len(numbers)//2
    if numbers[idx] == target:
        print(numbers[idx])
    elif numbers[idx] > target:
        binarySearch(numbers[:idx])
    elif numbers[idx] < target:
        binarySearch(numbers[idx+1:])


N, target = list(map(int, input().split()))
numbers = list(map(int, input().split()))
binarySearch(numbers)
