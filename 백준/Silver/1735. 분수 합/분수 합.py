import math

a, b = map(int, input().split())
c, d = map(int, input().split())

top = a*d + b*c
bottom = b*d

n = math.gcd(top, bottom)
top //= n
bottom //= n

print(top, bottom)