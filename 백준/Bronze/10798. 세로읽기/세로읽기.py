arr = [[] for _ in range(15)]
for _ in range(5):
    s = input()
    for i in range(len(s)):
        arr[i].append(s[i])

ans = ''

for i in range(len(arr)):
    ans += ''.join(arr[i])
print(ans)