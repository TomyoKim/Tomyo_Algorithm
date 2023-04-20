n = int(input())
a, b, c = map(int, input().split())
ans = 0
if n >= a:
    ans += a
else:
    ans += n

if n >= b:
    ans += b
else:
    ans += n
if n >= c:
    ans += c
else:
    ans += n

print(ans)
