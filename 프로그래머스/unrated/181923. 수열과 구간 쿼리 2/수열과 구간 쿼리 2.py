def solution(arr, queries):
    max_value = 10**9 + 1
    arr1 = [max_value] * len(queries)
    for i in range(len(queries)):
        for j in range(queries[i][0], queries[i][1]+1):
            if arr[j] > queries[i][2] and arr1[i] > arr[j]:
                arr1[i] = arr[j]
        if arr1[i] == max_value:
            arr1[i] = -1
    return arr1
