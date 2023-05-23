def solution(a, b):
    answer = 0
    ans1 = int(str(a) + str(b))
    ans2 = 2 * a * b
    if ans1 >= ans2:
        answer = ans1
    else:
        answer = ans2
    return answer