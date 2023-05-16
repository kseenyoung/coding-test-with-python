INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
result = 0

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         temp = graph[i][j]
#         print(temp if temp != INF else "INF", end=" ")
#     print()

for i in range(1, N+1):
    flag = True
    for j in range(1, N+1):
        if i != j:
            if graph[i][j] == INF and graph[j][i] == INF:
                flag = False
    if flag:
        result += 1

print(result)