def binSearch(arr, target):
    idx = len(arr)//2
    if len(arr) == 0:
        print('no', end=' ')
    elif arr[idx] == target:
        print('yes', end=' ')
    elif arr[idx] > target:
        binSearch(arr[:idx], target)
    elif arr[idx] < target:
        binSearch(arr[idx+1:], target)


N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

Ns.sort()
for i in range(M):
    binSearch(Ns, Ms[i])
