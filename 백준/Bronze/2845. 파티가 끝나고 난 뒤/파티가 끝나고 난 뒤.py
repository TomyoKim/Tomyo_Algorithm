l, p = map(int, input().split())
n = list(map(int, input().split()))
a = l * p

for i in n:
    print(i - a, end = ' ')