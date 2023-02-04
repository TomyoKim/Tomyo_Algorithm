cnt=1
temp = True
s = []
a = []

n = int(input())
for i in range(n):
    num = int(input())
    while cnt <= num:
        s.append(cnt)
        a.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        a.append('-')
    else:
        temp = False
        break
if temp == False:
    print("NO")
else:
    for i in a:
        print(i)

