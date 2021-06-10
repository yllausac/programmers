def solution(words, queries):
    answer = []
    for query in queries:
        key = list(query)
        count = 0
        for word in words:
            lyrics = list(word)
            if len(key) == len(lyrics):
                match = 0
                for i in range(len(key)):
                    if key[i] == '?' or key[i] == lyrics[i]:
                        match += 1
                    else:
                        break
                if match == len(key):
                    count += 1
        answer.append(count)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
