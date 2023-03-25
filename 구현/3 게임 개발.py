import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
A, B, D = list(map(int, input().split()))
tempD = D

board = []  # 실제 맵
tempBoard = [[0]*M for _ in range(N)]  # 방문한 맵***

# 현재 서 있는 위치 방문 표시
tempBoard[A][B] = 1
result = 1

for _ in range(N):
    board.append(list(map(int, input().split())))

# 북, 동, 남, 서 일 때 방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    D = 3 if D == 0 else D-1  # 왼쪽 방향
    A += dx[D]
    B += dy[D]

    if board[A][B] != 1 and tempBoard[A][B] != 1:  # 육지 & 방문 x
        result += 1
        tempBoard[A][B] = 1
        tempD = D
    else:
        A -= dx[D]
        B -= dy[D]
        if D == tempD:  # 360 돌았을 때
            break

print(result)
