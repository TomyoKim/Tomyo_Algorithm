import heapq
from sys import stdin

n = int(stdin.readline())
heap = []

for _ in range(n):
    n = int(stdin.readline())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)