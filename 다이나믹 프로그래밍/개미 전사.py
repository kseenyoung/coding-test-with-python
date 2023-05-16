n = int(input())
dp = [0]*(n+1)

number = list(map(int, input().split()))
dp[0] = number[0]
dp[1] = max(dp[0], number[1])

for i in range(2, n):
    dp[i] = max(number[i] + dp[i-2], dp[i-1])

print(dp[n-1])