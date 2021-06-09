def solution(p):
    if not p:
        return ""
    u, v = divide(p)
    if isBalanced(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

        return answer


def divide(p):
    lcount, rcount = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            lcount += 1
        else:
            rcount += 1
        if lcount == rcount:
            return p[:i+1], p[i+1:]


def isBalanced(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


print(solution("(()())()"))
