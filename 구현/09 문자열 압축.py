# 방법1 (74%)
def solution(s):
    result = len(s)
    for i in range(1, len(s) // 2 + 1):
        previous = s[:i]

        count = 1
        string = ''
        for j in range(i, len(s), i):
            if previous == s[j:j + i]:
                count += 1
            else:
                string += str(count) + previous
                previous = s[j:j + i]
                count = 1

        string += str(count) + s[j:]
        string = string.replace('1', '')  # 10, 11, 12 ... 문제 발생
        result = min(result, len(string))
    return result

# 방법2 : 1제거 하는 방식은 count가 2자리 이상일 때 문제가 발생한다. ex.10 -> 0, 12 -> 2 ...
def solution(s):
    result = len(s)
    for i in range(1, len(s) // 2 + 1):
        previous = s[:i]

        count = 1
        string = ''
        for j in range(i, len(s), i):
            if previous == s[j:j + i]:
                count += 1
            else:
                string += str(count) + previous if count != 1 else previous
                previous = s[j:j + i]
                count = 1

        string += str(count) + s[j:] if count != 1 else s[j:]
        # string = string.replace('1', '')  # 10, 11, 12 ... 문제 발생
        result = min(result, len(string))
    return result