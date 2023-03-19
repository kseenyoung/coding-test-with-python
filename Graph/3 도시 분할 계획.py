def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
edges = []

for i in range(M):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort()

parent = [i for i in range(N+1)]
cost = 0
last = 0  # 마지막 가장 큰 간선

for i, (w, a, b) in enumerate(edges):
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cost += w
        last = w

print(cost-last)  # 모든 간선 중 마지막 간선을 뺀다

# 입력 예시
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4