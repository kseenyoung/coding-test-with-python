# 단순 재귀 피보나치 O(2^N)
def pibonach(num):
    if num <= 2:
        return 1
    return pibonach(num-2) + pibonach(num-1)

print(pibonach(7))


# 재귀 다이나믹 피보나치(탑다운)
N = int(input("재귀 다이나믹 피보나치 수 : "))
d = [1] + [0]*N
def pibo(num):
    if num <= 2:
        return d[0]
    d[num] = pibo(num-1) + pibo(num-2)
    return d[num]

print(pibo(N))

# 반복 다이나믹 피보나치(바텀업)
N = int(input("반복 다이나믹 피보나치 수 : "))
d2 = [0, 1] + [0]*N
for i in range(2, N+1):
    d2[i] = d2[i-2] + d2[i-1]

print(d2[N])