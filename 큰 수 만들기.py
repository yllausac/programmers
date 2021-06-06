def solution(number, k):
    temp = []
    for i in number:
        while temp and temp[-1] < i and k > 0:
            temp.pop()
            k -= 1
        temp.append(i)
    while k > 0:
        temp.pop()
        k -= 1
    answer = "".join(temp)
    return answer


print(solution("4177252841", 4))
