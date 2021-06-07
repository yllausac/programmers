def solution(str1, str2):
    str1 = list(str1.lower())  # 소문자로 변환
    str2 = list(str2.lower())

    A, B = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i] + str1[i+1])

    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            B.append(str2[j] + str2[j+1])

    AiB = list(set(A) & set(B))
    AuB = list(set(A) | set(B))

    if len(AuB) == 0:
        return 65536
    icount = sum([min(A.count(i), B.count(i)) for i in AiB])
    ucount = sum([max(A.count(i), B.count(i)) for i in AuB])

    return int(icount/ucount * 65536)


print(solution("aa1+aa2", "AAAA12"))
