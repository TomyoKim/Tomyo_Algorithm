from collections import deque

def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    visited = [0] *(n+1)
    for a, b in edge:
        arr[a].append(b)
        arr[b].append(a)
        
    visited[1] = 1
    q = deque([1])
    
    while q:
        x = q.popleft()
        for nx in arr[x]:
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
    maxV = max(visited)
    cnt = visited.count(maxV)
    return cnt if cnt > 0 else 1