N, M, K = list(map(int, input().split()))

numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

# 내 풀이
# result = 0
#
# for m in range(1, M+1):
#     if m % K == 0:
#         result += numbers[1]
#     else:
#         result += numbers[0]
#
# print(result)

# 조금 더 효율적인 코드
count = (M // (K+1)) * K + (M % (K+1))  # 가장 큰 수가 더해질 횟수
result = count*numbers[0] + (M-count)*numbers[1]

print(result)
