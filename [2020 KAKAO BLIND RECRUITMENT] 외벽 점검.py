def solution(n, weak, dist):
    answer = 0
    table = [True for _ in range(n)]
    for i in weak:
        table[i] = False
    print(table)
    dist.reverse()
    print(dist)
    for friend in dist:
        for start in weak:
            while friend > 0:
                table[start] = True
                friend -= 1
                start += 1
            if False in table:
                continue
            else:
                return
        print(table)

    return answer


print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
