def find_parent(x):
    # 기본
    # if parent[x] != x:
    #     return find_parent(parent[x])
    # return x

    # 경로 압축 기법
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


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(a, b)

print('각 원소가 속한 집합: ', end=" ")
for i in range(1, v+1):
    print(find_parent(i), end=" ")

print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=" ")