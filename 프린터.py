from collections import deque


def solution(priorities, location):
    answer = 0
    printer = deque([(v, i) for i, v in enumerate(priorities)])

    while len(printer):
        item = printer.popleft()
        if printer and max(printer)[0] > item[0]:
            printer.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer


print(solution([1,1,9,1,1,1], 0))
