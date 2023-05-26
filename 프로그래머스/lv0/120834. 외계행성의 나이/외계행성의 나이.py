def solution(age):
    answer = ''
    answer = answer.join([chr(int(i)+97) for i in str(age)])
    return answer