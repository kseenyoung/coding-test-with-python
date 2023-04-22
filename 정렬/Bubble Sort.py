a = [1, 5, 3, 9, 6, 7, 8, 2, 4]

# Internet
for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a)

# What I learned in Basic Coding
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("result :", a)
