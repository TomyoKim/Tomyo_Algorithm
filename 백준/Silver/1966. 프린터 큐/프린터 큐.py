from collections import deque
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0

    while q:
        max_q = max(q)
        top = q.popleft()
        m -= 1
        if max_q != top:
            q.append(top)
            if m < 0:
                m = len(q)-1
        else:
            cnt += 1
            if m == -1:
                print(cnt)
                break