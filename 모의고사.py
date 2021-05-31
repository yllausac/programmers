def solution(answers):
    answer = []
    first, second, third = [], [], []
    while len(first) < len(answers):
        for i in range(1, 6):
            first.append(i)
    while len(second) < len(answers):
        for i in [2, 1, 2, 3, 2, 4, 2, 5]:
            second.append(i)
            if len(second) == len(answers):
                break
    while len(third) < len(answers):
        for i in [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]:
            third.append(i)
            if len(third) == len(answers):
                break

    count_one, count_two, count_three = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == first[i]:
            count_one += 1
        if answers[i] == second[i]:
            count_two += 1
        if answers[i] == third[i]:
            count_three += 1

    temp = max(count_one, count_two, count_three)
    if count_one == temp:
        answer.append(1)
    if count_two == temp:
        answer.append(2)
    if count_three == temp:
        answer.append(3)
    return answer


print(solution([1, 3, 2, 4, 2]))
