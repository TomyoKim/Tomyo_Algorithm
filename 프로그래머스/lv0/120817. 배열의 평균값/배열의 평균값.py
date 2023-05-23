def solution(numbers):
    answer = 0
    sumNumber = 0
    for i in numbers:
        sumNumber += i
    answer = sumNumber / len(numbers)
    return answer