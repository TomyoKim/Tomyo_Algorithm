def solution(array):
    answer = 0
    array.sort()
    a = len(array)
    b = a // 2
    answer = array[b]
    return answer