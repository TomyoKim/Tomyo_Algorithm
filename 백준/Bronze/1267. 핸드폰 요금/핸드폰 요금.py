n = int(input())

nList = list(map(int, input().split()))

y = 0
m = 0

for i in nList:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15

if y == m:
    print('Y M', m)
elif m < y:
    print('M', m)
else:
    print('Y', y)