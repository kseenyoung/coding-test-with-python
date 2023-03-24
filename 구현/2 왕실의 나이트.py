alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

pos = input()
position = [alpa.index(pos[0])+1, int(pos[1])]

result = 0
if position[0] < 7:  # down
    if position[1] < 8:
        result += 1
    if position[1] > 1:
        result += 1
if position[0] > 2:  # up
    if position[1] < 8:
        result += 1
    if position[1] > 1:
        result += 1
if position[1] < 7:  # right
    if position[0] < 8:
        result += 1
    if position[0] > 1:
        result += 1
if position[1] > 2: # left
    if position[0] < 8:
        result += 1
    if position[0] > 1:
        result += 1

print(result)