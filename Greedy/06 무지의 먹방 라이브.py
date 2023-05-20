from collections import deque
# 방법1 (효율성 실패)
def solution(food_times, k):
    que = deque()
    for i in range(len(food_times)):
        que.append((food_times[i], i+1))
    result = 0
    while que:
        q = que.popleft()
        if result == k:
            return q[1]
        if q[0] != 0:
            que.append((q[0]-1, q[1]))
            result += 1
    return -1


import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1


    length = len(food_times)  # 한 번의 로테이션을 위해 남은 음식 개수
    previous = 0  # 이전 처리 음식

    que = []
    for i, time in enumerate(food_times):  # (시간, 번호) 힙 삽입
        heapq.heappush(que, (time, i + 1))

    while k - (que[0][0] - previous) * length >= 0:
        time, now = heapq.heappop(que)  # 처리할 가장 작은 음식
        k -= (time - previous) * length
        previous = time
        length -= 1  # 한 번의 로테이션 처리

    que.sort(key=lambda x: x[1])  # 음식 번호로 재정렬
    return que[k % length][1]  # 남은 음식 수에 대한 로테이션 후 최종 위치


print(solution([3, 1, 2],	5))
print(solution1([3, 1, 2],	5))