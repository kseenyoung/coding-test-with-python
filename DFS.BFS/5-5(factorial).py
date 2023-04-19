def factorial(number):
    if number <= 0:
        return 1
    return factorial(number - 1) * number


print(factorial(int(input("구할 팩토리얼 숫자 입력하시오 : "))))
