def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n - i:
            return n - i

    return 0


print(solution([20, 19, 18, 1]))
