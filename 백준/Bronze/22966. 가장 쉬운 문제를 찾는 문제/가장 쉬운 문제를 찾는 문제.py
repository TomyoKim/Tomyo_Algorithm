n = int(input())

nList = []

for i in range(n):
    nList.append(input().split())

nList=sorted(nList, key= lambda x:x[1])

print(nList[0][0])