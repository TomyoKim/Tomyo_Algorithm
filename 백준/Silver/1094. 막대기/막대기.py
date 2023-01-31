x = int(input())
answer = 0
while x != 0:
    if x % 2 == 1:
        answer += 1
    x = x // 2
print(answer)