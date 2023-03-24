m, s = 0, 0
N = int(input())

result = 0

while m != 59 or s != 59 or N:
    stringM = str(s)
    stringS = str(m)
    stringH = str(N)

    if '3' in stringS or '3' in stringM or '3' in stringH:  # '시'도 카운드 해야 함  #'3' in stringH + stringM + stringS
        result += 1

    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        N -= 1
        m = 0

print(result)
