from collections import deque
m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()

ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


bfs()

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans -1)