n, m=map(int, input().split())

s=set(input() for _ in range(n))

ans=0

for _ in range(m):
    check_list=input()
    if check_list in s:
        ans+=1
        
print(ans)