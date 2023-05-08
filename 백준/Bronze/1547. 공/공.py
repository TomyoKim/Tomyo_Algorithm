n = int(input())

cup = [1, 2, 3]

for _ in range(n):
    x, y = map(int, input().split())

    xn = cup.index(x)
    yn = cup.index(y)

    cup[xn], cup[yn] = cup[yn], cup[xn]

print(cup[0])