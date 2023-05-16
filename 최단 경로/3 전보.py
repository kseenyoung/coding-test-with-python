import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for i in range(M):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)
result = 0
cnt = 0
for i in range(1, N+1):
    if distance[i] != INF:
        cnt += 1
    result = max(distance[i], result)

print(cnt-1, result)