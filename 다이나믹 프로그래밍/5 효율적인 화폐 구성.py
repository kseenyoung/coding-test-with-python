N, M = list(map(int, input().split()))
coins = [10001]*(M+1)
coins[0] = 0
nums = []

for i in range(N):
    nums.append(int(input()))

for i in range(N):  # 각 coin
    coin = nums[i]
    for target in range(coin, M+1):  # 해당하는 coin부터 M까지
        coins[target] = min(coins[target - coin]+1, coins[target])

print(coins[M] if coins[M] != 10001 else -1)
