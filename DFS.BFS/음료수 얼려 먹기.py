N, M = list(map(int, input().split()))
frame = []
visited = set()
count = 0

dr = [1, 0, -1, 0]  # down, right, up, left
dc = [0, 1, 0, -1]

frame.append([1]*(M+2))
for i in range(N):
    frame.append([1] + list(int(i) for i in input()) + [1])
frame.append([1]*(M+2))


def dfs(i, j):
    if (i, j) not in visited and N >= i > 0 and M >= j > 0:  # 1 <= i <= N, 1: <= j <= M
        visited.add((i, j))
        for direction in range(4):
            i += dr[direction]
            j += dc[direction]
            if frame[i][j] == 0:
                dfs(i, j)


for i in range(1, N+1):
    for j in range(1, M+1):
        if frame[i][j] == 0 and (i, j) not in visited:
            dfs(i, j)
            count += 1

print(count)
