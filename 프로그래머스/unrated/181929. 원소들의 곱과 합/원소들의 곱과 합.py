def solution(num_list):
    answer = 0
    ans1 = sum(num_list) ** 2
    ans2 = 1
    for i in num_list:
        ans2 *= i
    if ans1 > ans2:
        answer = 1
    elif ans1 < ans2:
        answer = 0
    return answer