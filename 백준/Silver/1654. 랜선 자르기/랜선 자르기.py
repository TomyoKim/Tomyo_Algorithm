k, n=map(int, input().split())

lan=[]

for _ in range(k):
    lan.append(int(input()))

l=1
r=max(lan)

while(l<=r):
    mid=(l+r)//2
    cnt=0

    for i in lan:
        cnt+=i//mid
        
    if cnt>=n:
        l=mid+1

    else:
        r=mid-1
print(r)