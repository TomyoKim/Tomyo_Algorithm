def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        sliceStr = i[s:s+l]
        num = int(sliceStr)
        if num > k:
            answer.append(num)
    return answer