def solution(brown, yellow):
    tile = brown + yellow
    for hori in range(tile, 2, -1):
        if tile % hori == 0:
            vertical = tile // hori
            if yellow == (hori-2)*(vertical-2):
                return[hori, vertical]


print(solution(24, 24))
