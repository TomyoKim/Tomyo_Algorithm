def solution(arr, queries):
    for i in range(len(queries)):
        a = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = a
    return arr
