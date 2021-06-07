def checktr(time, li):
    task = 0
    start = time
    end = time + 1000  # 1초동안의 처리량을 계산하기 위함
    for i in li:
        if i[1] >= start and i[0] < end:
            task += 1
    return task


def solution(lines):
    li = []
    answer = 1
    for line in lines:
        y, a, b = line.split()
        a = a.split(':')
        b = float(b.replace('s', ''))*1000
        end = (int(a[0])*3600 + int(a[1]) * 60 + float(a[2]))*1000
        start = end - b + 1
        li.append([start, end])

    for i in li:
        answer = max(answer, checktr(i[0], li), checktr(i[1], li))

    return answer


print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
