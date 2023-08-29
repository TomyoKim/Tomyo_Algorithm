def solution(my_string, is_suffix):
    answer = []
    result = 0
    for i in range(1, len(my_string)+1):
        answer.append(my_string[i-1::])
        
    for i in answer:
        if i == is_suffix:
            result = 1
            
    return result