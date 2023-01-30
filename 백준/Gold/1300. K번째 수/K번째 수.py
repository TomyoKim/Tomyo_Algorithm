n = int(input())
k = int(input())

def binary_search(start, end):
    while start <= end:
        mid = (start + end)//2

        cnt = 0

        for i in range(1, n+1):
            cnt += min(mid//i, n)
            '''m//i는 i*(m//i)
            i번째 행에 있는 값은 i*j
            i번째 행의 최댓값은 i*m
            i번째 행에서 m보다 작은 값으 개수는 m//i 또는 n'''

        if cnt >= k:
            end = mid-1
        else:
            start = mid+1

    return start

print(binary_search(1, k))