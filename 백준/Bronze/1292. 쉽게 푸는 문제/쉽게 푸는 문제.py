a, b = map(int, input().split())
nList = []

for i in range(b+1):
    for j in range(i):
        if len(nList) == b:
            break
        nList.append(i)
print(sum(nList[a-1:b]))