n, m = map(int, input().split())

wood_h = list(map(int, input().split()))


def binary_search(start, end):
    while start <= end:
        mid = (start+end)//2
        wood_sum = 0
        for i in wood_h:
            if i >= mid:
                wood_sum += i-mid
                
        if wood_sum >= m:
            start = mid+1
        else:
            end = mid-1
    return(end)

print(binary_search(1, max(wood_h)))