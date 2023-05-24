def solution(a, d, included):
    answer = 0
    arr = [0] * len(included)
    for i in range(len(included)):
        if i == 0:
            arr[i] = a
        else:
            arr[i] = arr[i-1]+d
        if included[i] == True:
            answer += arr[i]
    return answer