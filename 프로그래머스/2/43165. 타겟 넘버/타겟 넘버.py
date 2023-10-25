from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    while q:
        i, v = q.popleft()
        if i == len(numbers) and v == target:
            answer += 1
        elif i == len(numbers):
            pass
        else:
            q.append((i + 1, v + numbers[i]))
            q.append((i + 1, v - numbers[i]))
    return answer