a = [1, 5, 3, 9, 6, 7, 8, 2, 4]

for i in range(len(a)):
    minIndex = i
    for j in range(i, len(a)):
        if a[minIndex] > a[j]:
            minIndex = j
    a[minIndex], a[i] = a[i], a[minIndex]

print("result : ", a)
