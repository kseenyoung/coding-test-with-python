n = int(input())
students = [[] for i in range(101)]

for i in range(n):
    student = input().split()
    students[int(student[1])].append(student[0])

for i in range(101):
    for s in students[i]:
        print(s, end=' ')
        