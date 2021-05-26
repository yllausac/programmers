def solution(clothes):
    category = {}
    for i in clothes:
        if i[1] in category:
            category[i[1]] += 1
        else:
            category[i[1]] = 1
    item = 1
    for i in category.values():
        item *= (i+1)

    return item - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
