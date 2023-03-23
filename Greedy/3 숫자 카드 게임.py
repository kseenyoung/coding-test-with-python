import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
minNum = 0

cards = []
for _ in range(N):
    line = list(map(int, input().split()))
    cards.append(line)

    if min(line) > minNum:
        minNum = min(line)

print(minNum)

