def solution(number):
    answer = 0
    n = 0
    number = list(number)
    for i in number:
        n += int(i)
    answer = n % 9
    return answer