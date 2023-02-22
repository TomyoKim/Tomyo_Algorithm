h = []

for _ in range(9):
    h.append(int(input()))
for i in h:
    for j in h:
        if sum(h) - i - j ==100 and i != j:
            h.remove(i)
            h.remove(j)
h.sort()
for i in h:
    print(i)