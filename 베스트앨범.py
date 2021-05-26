def solution(genres, plays):
    answer = []
    song = {}
    best_genres = {}
    for i in range(len(genres)):
        song[i] = [genres[i], plays[i]]
        if genres[i] in best_genres:
            best_genres[genres[i]] += plays[i]
        else:
            best_genres[genres[i]] = plays[i]

    best_genres = sorted(best_genres.items(), key=lambda x:x[1], reverse=True)
    song = sorted(song.items(), key=lambda x:(x[1][0], -x[1][1]))

    for i in best_genres:
        count = 0
        for j in song:
            if j[1][0] == i[0]:
                answer.append(j[0])
                count += 1
            if count >= 2:
                break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [5000, 600, 150, 800, 2500]))
