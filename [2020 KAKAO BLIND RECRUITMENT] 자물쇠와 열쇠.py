def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    expandSize = len(lock) + start * 2

    for i in range(0, 4):
        for k in range(end):
            for d in range(end):
                if move(k, d, key, lock, expandSize, start, end):
                    return True
        key = turn(key)

    return False


def turn(key):
    m = len(key)
    temp = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            temp[j][m-1-i] = key[i][j]
    key = temp
    return key


def move(startX, startY, key, lock, expandSize, start, end):
    expandList = [[0]*expandSize for _ in range(expandSize)]

    for i in range(len(key)):
        for j in range(len(key)):
            expandList[startX + i][startY + j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            expandList[i][j] += lock[i - start][j - start]
            if expandList[i][j] != 1:
                return False
    return True


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
