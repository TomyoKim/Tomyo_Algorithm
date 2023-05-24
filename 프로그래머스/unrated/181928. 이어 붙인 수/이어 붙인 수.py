def solution(num_list):
    answer = 0
    ans1 = ''
    ans2 = ''
    for i in num_list:
        if i % 2 == 0:
            ans1 += str(i)
        else:
            ans2 += str(i)
    answer = int(ans1) + int(ans2)
    return answer