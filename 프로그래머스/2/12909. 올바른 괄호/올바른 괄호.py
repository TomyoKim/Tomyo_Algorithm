def solution(s):
    ans = 0
    for i in s:
        if ans < 0:
            break
        ans = ans + 1 if i=="(" else ans - 1 if i == ")" else ans
    return ans == 0