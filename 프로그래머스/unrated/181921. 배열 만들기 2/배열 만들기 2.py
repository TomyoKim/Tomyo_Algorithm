def solution(l, r):
    answer = []
    for i in range(l, r+1):
        str_num = str(i)
        cnt = 0
        for j in range(len(str_num)):
            if str_num[j] == '0' or str_num[j] == '5':
                cnt += 1
        if cnt == len(str_num):
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer