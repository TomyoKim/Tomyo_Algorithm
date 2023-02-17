n = int(input())
nList = list(map(int, input().split()))
ans = 0
nList.sort()
for i in range(n):
    for j in range(i+1):
        ans += nList[j]
print(ans)