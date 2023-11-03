def solution(name):
    answer = 0
    m = len(name) - 1

    for i, c in enumerate(name):
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        n = i + 1
        while n < len(name) and name[n] == 'A':
            n += 1
        m = min([m, 2 * i + len(name) - n, i + 2 * (len(name) - n)])

    answer += m
    return answer