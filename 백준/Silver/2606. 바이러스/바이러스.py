from collections import deque
n = int(input())
node_pair = int(input())
# Initialize visited array
visited = [0] * (n + 1)

isConnected = [[0] * (n + 1) for i in range(n + 1)]


# isConnected[i][j] i and j are connected
def BFS(cur_node):
    cnt=0
    q = deque()
    q.append(cur_node)
    while len(q):
        cur_node = q.popleft()
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        cnt+=1
        # isConnected[i][j] i and j are connected
        for next_node in range(1, n+1):
            if isConnected[cur_node][next_node] == 1 and cur_node != next_node and not visited[next_node]:
                q.append(next_node)

    return cnt

for _ in range(node_pair):
    a, b = map(int, input().split())
    # fill isConnected information
    isConnected[a][b] = isConnected[b][a] = 1

print(BFS(1)-1)