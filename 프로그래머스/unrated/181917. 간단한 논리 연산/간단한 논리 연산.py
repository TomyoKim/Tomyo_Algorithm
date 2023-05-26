def solution(x1, x2, x3, x4):
    answer = True
    if (x1 or x2 == True) and (x3 or x4 == True):
        answer = True
    else:
        answer = False
    return answer