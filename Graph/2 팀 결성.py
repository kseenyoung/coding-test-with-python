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
parent = [i for i in range(N+1)]

for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 0 and find_parent(a) != find_parent(b):
        union_parent(a, b)
    if op == 1:
        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")


# 입력 예제
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1