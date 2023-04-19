N, M, K, X = list(map(int, input().split()))  # 도시 개수, 도로 개수, 거리 정보, 출발 도시
graph = [[] for _ in range(N+1)]  # 인접 행렬
visited = [False]*(N+1)

for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

def bfs(depth, vertex):
    visited[vertex] = True
    if depth == K:
        print(vertex, end=' ')

    for v in graph[vertex]:
        if v not in visited:  # 방문하지 않은 노드
            bfs(depth+1, v)


bfs(0, X)
