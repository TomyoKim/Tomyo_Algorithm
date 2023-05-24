def solution(money):
    answer = []
    i = money // 5500
    j = money % 5500
    answer.append(i)
    answer.append(j)
    return answer