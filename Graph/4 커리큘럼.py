# 위상 정렬
from collections import deque
import copy

n = int(input())
indegree = [0]*(n+1)  # 진입 차수
graph = [[] for i in range(n+1)]  # 연결된 노드
time = [0]*(n+1)  # 각 과목의 소요 시간

for i in range(1, n+1):
    alist = list(map(int, input().split()))
    time[i] = alist[0]
    for a in alist[1:-1]:
        indegree[i] += 1
        graph[a].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()