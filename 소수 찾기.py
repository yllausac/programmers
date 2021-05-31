from itertools import permutations
import math


def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    prime_number = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                prime_number.append(int(i))

    answer = len(set(prime_number))
    return answer


print(solution("011"))
