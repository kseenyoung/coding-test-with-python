from collections import deque
import heapq
dr = [1, -1, 0, 0]  # down, up, right, left
dc = [0, 0, 1, -1]
INF = int(1e9)

for test in range(int(input())+1):
    n = int(input())
    graph = [[] for _ in range(n+1)]  # 방문을 위해 필요한 비용
    visited = [[INF]*n for _ in range(n)]  # -1 -> INF, 1에서 다음 노드 까지 가기 위한 최소 거리(다익스트라)
    que = []

    for i in range(n):  # 방문을 위해 필요한 비용 초기화
        graph[i] = list(map(int, input().split()))


    heapq.heappush(que, (graph[0][0], 0, 0))  # 우선순위 큐 초기화
    visited[0][0] = graph[0][0]  # 1번 노드 방문 표시

    while que:
        w, row, col = heapq.heappop(que)
        # print((row, col), w, end=" ")
        if visited[row][col] < w:
            continue
        for d in range(4):  # row, col 위치에서 아래, 위, 오른, 왼
            r = row + dr[d]
            c = col + dc[d]

            if -1 < r < n and -1 < c < n:  # 범위를 넘지 않았다면
                cost = w + graph[r][c]  # 해당 위치 최소 비용 + 이동시 필요한 비용
                if visited[r][c] > cost:
                    visited[r][c] = cost
                    heapq.heappush(que, (cost, r, c))

    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print(visited[n-1][n-1])
