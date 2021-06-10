def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    graphsize = len(lock) + start * 2

    for i in range(0, 4):
        for k in range(end):
            for d in range(end):
                if move(k, d, key, lock, graphsize, start, end):
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


def move(X, Y, key, lock, graphsize, start, end):
    graph = [[0] * graphsize for _ in range(graphsize)]

    for i in range(len(key)):
        for j in range(len(key)):
            graph[X + i][Y + j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            graph[i][j] += lock[i - start][j - start]
            if graph[i][j] != 1:
                return False
    return True


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
