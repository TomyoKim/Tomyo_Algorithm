n, k = map(int, input().split())
nList = []
for i in range(1, n+1):
    if n%i == 0:
        nList.append(i)

if len(nList) >= k:
    print(nList[k-1])
else:
    print(0)