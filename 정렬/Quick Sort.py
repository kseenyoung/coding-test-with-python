a = [5, 1, 3, 9, 6, 7, 8, 2, 4]


# 공식 퀵 정렬
def dfs(start, end):
    if start < end:
        pivot = a[start]
        L, R = start+1, end
        while R > L:
            while R > start and a[R] > pivot:  # pivot 보다 작은 값 위치 찾기
                R -= 1
            while L <= end and a[L] < pivot:  # pivot 보다 큰 값 위치 찾기
                L += 1

            if R < L:  # 위치가 엇갈렸다면 둘의 위치 교환
                a[R], a[start] = a[start], a[R]
            else:
                a[R], a[L] = a[L], a[R]
        dfs(start, R-1)
        dfs(L, end)


dfs(0, len(a)-1)
print(a)


# Pythonic 퀵 정렬
def dfs(arr):
    if len(arr) > 1:
        pivot = arr[0]
        tail = arr[1:]

        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]

        return dfs(left_side) + [pivot] + dfs(right_side)
    else:  # 원소가 1개 이하의 리스트
        return arr


b = dfs(a)
print(b)
