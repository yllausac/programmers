# 효율성 테스트 3문제 미통과

def solution(words, queries):
    answer = []
    key, value = [], []
    for word in words:
        key.append(list(word))
    for query in queries:
        value.append(list(query))

    for item in value:
        m = len(item)
        count = 0
        for target in key:
            match = 0
            if len(target) == m:
                for i in range(m):
                    if target[i] == item[i] or item[i] == '?':
                        match += 1
                if match == m:
                    count += 1
        answer.append(count)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
