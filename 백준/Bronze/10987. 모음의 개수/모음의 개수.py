n = input()
aeiou = ['a', 'e', 'i', 'o', 'u']
ans = 0
for i in n:
    if i in aeiou:
        ans+=1
        
print(ans)        