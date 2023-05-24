def solution(num_list):
    answer = []
    e = 0
    o = 0
    for i in num_list:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    answer.append(e)
    answer.append(o)
    return answer