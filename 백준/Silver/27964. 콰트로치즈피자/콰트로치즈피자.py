n = int(input())

toping = list(map(str, input().split()))

cheese_toping = []

for i in toping:
    if 'Cheese' in i:
        if i.endswith('Cheese', 0, len(i)+1) is True:
            cheese_toping.append(i)

ans = len(set(cheese_toping))

if ans >= 4:
    print('yummy')
else:
    print('sad')