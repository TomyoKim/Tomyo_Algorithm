n = list(map(int, input()))
nLen = len(n)

if nLen == 1:
    print('NO')
else:
    a = b = 1
    for i in range(nLen - 1):
        a = b = 1
        for j in range(i + 1):
            a *= n[j]
        for k in range(i + 1, nLen):
            b *= n[k]
        if a == b:
            break
    if a == b:
        print('YES')
    else:
        print('NO')