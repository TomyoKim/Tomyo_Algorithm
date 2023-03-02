n=int(input())

nList = list(map(int,input().split()))
nList = list(set(nList))
nList.sort()

for i in nList:
    print(i,end=' ')