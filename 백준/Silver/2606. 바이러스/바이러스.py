from collections import deque

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(i):
    q = deque([i])
    cnt = 0
    visited[i] = True
    while q:
      x = q.popleft()
      for nx in arr[x]:
          if not visited[nx]:
              visited[nx] = True
              q.append(nx)
              cnt += 1

    return cnt

print(bfs(1))