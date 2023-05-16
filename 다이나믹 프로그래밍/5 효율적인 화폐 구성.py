N, M = list(map(int, input().split()))
coins = [10001]*(M+1)

for i in range(N):
    coins[i+1] = int(input())

for i in range(2, M+1):
    for j in range(i, M+1):
        coins[i] = min(coins[j-i], coins[j])

print(coins[M])