def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    result = []
    
    for i, ans in enumerate(answers):
        if s1[i % 5] == ans:
            score[0] += 1
        if s2[i % 8] == ans:
            score[1] += 1
        if s3[i % 10] == ans:
            score[2] += 1

    for i, s in enumerate(score):
        if s == max(score):
            result.append(i + 1)

    return result