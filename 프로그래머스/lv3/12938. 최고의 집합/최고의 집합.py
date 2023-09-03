def solution(n, s):
    if n > s: return [-1]
    result = []
    a = s // n
    for _ in range(n):
        result.append(a)
    b = len(result) - 1
    for _ in range(s % n):
        result[b] += 1
        b -=1
    return result