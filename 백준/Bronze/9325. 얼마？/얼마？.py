t=int(input())
for i in range(t):
    s=int(input())
    n=int(input())
    ans=s
    for j in range(n):
        p, q=map(int, input().split())
        ans+=p*q
    print(ans)