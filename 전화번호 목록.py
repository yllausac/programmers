def solution(phone_book):
    answer = True
    phone_number = {}
    for i in phone_book:
        phone_number[i] = True
    for i in phone_book:
        temp = ''
        for number in i:
            temp += number
            if temp in phone_number and temp != i:
                answer = False
    return answer


print(solution(["12","123","1235","567","88"]))
