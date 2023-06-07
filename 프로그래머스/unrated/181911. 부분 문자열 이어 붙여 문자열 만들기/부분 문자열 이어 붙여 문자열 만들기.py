def solution(my_strings, parts):
    answer = ''
    for i, j in enumerate(parts):
        a, b = parts[i][0], parts[i][1]+1
        answer += my_strings[i][a:b]
    return answer