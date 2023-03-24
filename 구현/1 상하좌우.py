N = int(input())
move = list(input().split())
position = [1, 1]

for m in move:
    if m == 'R' and position[1] < N:
        position[1] += 1
    elif m == 'U' and position[0] > 1:
        position[0] -= 1
    elif m == 'D' and position[0] < N:
        position[0] += 1
    elif m == 'L' and position[1] > 1:
        position[1] -= 1

print(position[0], position[1])
