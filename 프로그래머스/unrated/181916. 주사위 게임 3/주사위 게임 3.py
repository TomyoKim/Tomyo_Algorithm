def solution(a, b, c, d):
    answer = 0
    if a == b == c == d:
        answer = 1111*a
    elif a == b and b == c:
            answer = (10 * a + d) ** 2
    elif a == d and d == c:
        answer = (10 * a + b) ** 2
    elif b == d and d == c:
        answer = (10 * d + a) ** 2
    elif a == d and d == b:
        answer = (10 * a + c) ** 2
    elif a == b and c == d:
        answer = (a + c) * abs(a - c)
    elif a == c and b == d:
        answer = (a + b) * abs(a - b)
    elif a == d and c == b:
        answer = (a + c) * abs(a - c)
    elif a == b and a != c and a != d and c != d:
        answer = c * d
    elif a == c and a != b and a != d and b != d:
        answer = b * d
    elif a == d and a != b and a != c and b != c:
        answer = b * c
    elif b == c and b != a and b != d and a != d:
        answer = a * d
    elif b == d and b != a and b != c and a != c:
        answer = a * c
    elif c == d and c != b and c != a and a != b:
        answer = a * b
    else:
        min_val = min(a, b, c, d)
        answer = min_val
    return answer
