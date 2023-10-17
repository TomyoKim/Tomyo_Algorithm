from collections import deque

t = int(input())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not in_range(nx, ny):
                continue
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0

    return

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)