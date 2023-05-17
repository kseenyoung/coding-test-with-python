def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v+1):
    parent[i] = i

cycle = False
for i in range(1, v+1):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        cycle = True
        break
    else:
        union_parent(a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 x")
