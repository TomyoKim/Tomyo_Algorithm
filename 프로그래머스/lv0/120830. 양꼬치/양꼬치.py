def solution(n, k):
    answer = 0
    a = n // 10
    k -= a
    answer = n * 12000 + k * 2000
    return answer