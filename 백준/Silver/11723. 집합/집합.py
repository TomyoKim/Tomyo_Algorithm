import sys
input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    a = input().split()
    if a[0] == 'all':
        s = set([i for i in range(1, 21)])
    elif a[0] == 'empty':
        s = set()
    elif a[0] == 'add':
        s.add(int(a[1]))
    elif a[0] == 'check':
        print(1 if int(a[1]) in s else 0)
    elif a[0] == 'remove':
        s.discard(int(a[1]))
    elif a[0] == 'toggle':
        if int(a[1]) in s:
            s.discard(int(a[1]))
        else:
            s.add(int(a[1]))