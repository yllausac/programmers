def solution(n, t, m, timetable):
    crew = [int(time.split(":")[0])*60 + int(time.split(":")[1]) for time in timetable]
    crew.sort()
    suttle = [(540+t*i, 0, None) for i in range(n)]  # 09:00부터 시작이므로
    suttleidx, crewidx = 0, 0
    while crewidx < len(crew):
        c = crew[crewidx]
        if suttleidx == len(suttle):
            break
        if c <= suttle[suttleidx][0] and suttle[suttleidx][1] < m:
            time, cnt, _ = suttle[suttleidx]
            suttle[suttleidx] = (time, cnt+1, c)
            crewidx += 1
        else:
            suttleidx += 1

    ret = suttle[-1][0]
    if suttle[-1][2]:
        if suttle[-1][1] == m:
            ret = suttle[-1][2] - 1

    return '%02d:%02d' % (ret // 60, ret % 60)


print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
