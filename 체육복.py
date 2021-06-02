def solution(n, lost, reserve):
    _reserve = [i for i in reserve if i not in lost]
    _lost = [i for i in lost if i not in reserve]
    for i in _reserve:
        a = i - 1
        b = i + 1
        if a in _lost:
            _lost.remove(a)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)


print(solution(5, [2, 4], [1, 3, 5]))
