def solution(s):
    length = []
    if len(s) == 1:
        return len(s)
    for size in range(1, len(s)//2 + 1):
        string = [s[i:i+size] for i in range(0, len(s), size)]
        count = 1
        compressed = ''
        for j in range(1, len(string)):
            prev, cur = string[j-1], string[j]
            if prev == cur:
                count += 1
            else:
                compressed += (str(count)+prev if count > 1 else prev)
                count = 1

        compressed += (str(count) + string[-1] if count > 1 else string[-1])
        length.append(len(compressed))
    return min(length)


print(solution("ababcdcdababcdcd"))
