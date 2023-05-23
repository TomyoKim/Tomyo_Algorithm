def solution(array):
    cnt = [0] * (max(array) + 1)
    for i in array:
        cnt[i] += 1
    m = 0
    for j in cnt:
        if j == max(cnt):
            m += 1
    if m > 1:
        return -1
    else:
        return cnt.index(max(cnt))