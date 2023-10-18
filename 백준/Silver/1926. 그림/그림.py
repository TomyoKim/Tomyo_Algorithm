from collections import deque

n, m = map(int, input().split())
q = deque()
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(arr, a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    cnt = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not in_range(nx, ny):
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

paint = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            paint.append(bfs(arr, i, j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))