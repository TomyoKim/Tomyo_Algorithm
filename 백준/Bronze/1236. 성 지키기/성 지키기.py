n, m = map(int, input().split())
castle = []

for _ in range(n):
    castle.append(input())

r, c = 0, 0

for i in range(n):
    if 'X' not in castle[i]:
        r += 1

for j in range(m):
    if 'X' not in [castle[i][j] for i in range(n)]:
        c += 1

print(max(r, c))