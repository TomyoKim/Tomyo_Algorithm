def solution(s):
    arr = s.split(" ")
    ans = []
    for i in arr :
        ans.append(i.capitalize())
    return ' '.join(ans)