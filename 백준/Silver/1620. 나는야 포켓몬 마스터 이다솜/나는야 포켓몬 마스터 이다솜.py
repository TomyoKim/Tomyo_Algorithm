import sys

input = sys.stdin.readline
n, m = map(int, input().split())

num = {}
name = {}

for i in range(1, n+1):
    pokemon = input().strip()
    num[pokemon] = i
    name[i] = pokemon

for _ in range(m):
    x = input().strip()
    if x.isdigit():
        print(name[int(x)])
    else:
        print(num[x])