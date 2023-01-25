n, m=map(int, input().split())

a_set = set()
b_set = set()
for _ in range(n):
    a_set.add(input())
    
for _ in range(m):
    b_set.add(input())

sum_ab=sorted(list(a_set & b_set))
print(len(sum_ab))

for i in sum_ab:
    print(i)