t=int(input())
cnt=0
for i in range(t):
    a, b=map(int, input().split())
    cnt+=1
    print('Case {0}: {1}'.format(cnt, a+b))