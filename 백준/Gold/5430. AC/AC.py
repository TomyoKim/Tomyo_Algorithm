from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    nList = deque(input()[1:-1].split(','))
    
    flag = 0
    
    if n == 0:
        nList = []
        
    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(nList) == 0:
                print('error')
                break
            else:
                 if flag % 2 == 0:
                     nList.popleft()
                 else:
                     nList.pop()
                     
    else:
        if flag % 2 == 0:
            print('[' + ','.join(nList) + ']')
        else:
            nList.reverse()
            print('[' + ','.join(nList) + ']')