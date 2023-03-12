import heapq
from sys import stdin

n = int(stdin.readline())
heap = []

for _ in range(n):
    a = int(stdin.readline())

    if a == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [-a, a])