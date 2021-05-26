def solution(participant, completion):
    answer = []
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            answer.append(i)
    print(answer)


solution(["leo", "kiki", "eden"], ["eden", "kiki"])
