numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))

numbers.sort(reverse=True)
for n in numbers:
    print(n, end=" ")
