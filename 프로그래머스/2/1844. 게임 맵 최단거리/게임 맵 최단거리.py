from collections import deque

def solution(maps):
    answer = 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    
    n = len(maps)
    m = len(maps[0])
    
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
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
        return maps[n-1][m-1]
    
    answer = bfs(0, 0)
                
    return -1 if answer == 1 else answer  