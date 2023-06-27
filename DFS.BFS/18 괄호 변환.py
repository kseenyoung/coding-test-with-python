# 풀이(20% -> 100%) : 38번째 줄 ( + swap_par(u[1:-1]) + ) + v   ->   ( + v + ) + swap_par(u[1:-1])
def check(par):
    stack = []
    for p in par:
        if p == '(':
            stack.append('(')
        elif p == ')' and stack:
            stack.pop()
        else:  # stack에 괄호가 없을 때
            return False
    return True


def swap_par(par):
    answer = ''
    for p in par:
        answer += '(' if p == ')' else ')'
    return answer


def dfs(par):
    if par == '':
        return par

    start = par[0]
    stack = 0

    for i, a in enumerate(par, start=1):
        stack += 1 if a == start else -1
        if not stack:  # 균형잡힌 괄호 문자열
            u, v = par[:i], par[i:]
            break

    v = dfs(v)
    if check(u):
        return u + v
    else:
        return '(' + v + ')' + swap_par(u[1:-1])   # 문제를 꼼꼼히 보자


def solution(p):
    return dfs(p)


solution("(()())()")
solution("()))((()")