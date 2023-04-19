from collections import deque
import math
N, M = list(map(int, input().split()))
count = math.inf  # 경로 중 가장 짧은 거리 값 저장

que = deque()
que.append(((0, 0), 1))

# 방문 표시
visited = set()
visited.add((0, 0))

# 맵 정보
board = []
for _ in range(N):
    board.append([int(i) for i in input()])

dr = [1, -1, 0, 0]  # 이동할 방향: down, up, right, left
dc = [0, 0, 1, -1]

# BFS
while que:
    q = que.popleft()
    if q[0] == (N-1, M-1):  # 시작위치: (0, 0) 도착위치: (N-1, M-1)
        count = min(count, q[1])
    else:
        for direction in range(4):  # 네 방향 별 확인
            i = q[0][0] + dr[direction]
            j = q[0][1] + dc[direction]
            if -1 < i < N and -1 < j < M and board[i][j] == 1 and (i, j) not in visited:
                # 벽을 넘어가지 않고 장애물 없고 방문하지 않았다면
                visited.add((i, j))
                que.append(((i, j), q[1]+1))

print(count)
