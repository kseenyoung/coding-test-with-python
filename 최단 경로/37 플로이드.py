import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]  # 인접 행렬

for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1][v2] = min(graph[v1][v2], w)  # (주의) 동일한 노선의 간선 있음

for k in range(1, n+1):  # 거쳐갈 노드
    for a in range(1, n+1):  # 시작 노드
        for b in range(1, n+1):  # 종료 노드
            # (a -> k -> b) 와 (a -> b) 비교하여 작은 값 대입
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) if a != b else 0

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=" ")  # INF라면 0 출력
    print()