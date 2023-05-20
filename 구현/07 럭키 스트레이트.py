N = str(input())

right, left = 0, 0
for i in range(len(N)//2):
    right += int(N[i])
    left += int(N[len(N)-1-i])

if right == left:
    print("LUCKY")
else:
    print("READY")