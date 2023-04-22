a = [1, 5, 3, 9, 6, 7, 8, 2, 4]

for i in range(len(a)):
    j = i
    while j != 0 and a[j] < a[j-1]:
        a[j-1], a[j] = a[j], a[j-1]
        j -= 1

print(a)
