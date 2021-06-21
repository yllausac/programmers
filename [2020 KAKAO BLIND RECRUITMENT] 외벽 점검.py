def solution(n, weak, dist):
    from itertools import permutations
    answer = len(dist) + 1  # 점검이 불가능한 경우
    weak_length = len(weak)

    # 길이를 두배로 늘리면 방향을 고려할 필요가 없다.
    for i in range(weak_length):
        weak.append(weak[i] + n)

    # dist의 모든 경우의 수
    dist_combin = list(map(list, permutations(dist, len(dist))))

    for i in range(weak_length):
        # 시작점을 하나씩 바꾸면서, weak의 길이만큼 잘라서 사용
        start = [weak[j] for j in range(i, i+weak_length)]
        for dist_p in dist_combin:
            result = 1
            dist_distance = 0  # 거리
            check_len = start[0] + dist_p[0]  # dist의 친구가 확인할 수 있는 최대 거리

            for k in range(weak_length):
                if start[k] > check_len:
                    result += 1
                    if result > len(dist_p):
                        break
                    dist_distance += 1
                    check_len = start[k] + dist_p[dist_distance]

            answer = min(answer, result)

    if answer > len(dist):
        return -1
    return answer


print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
