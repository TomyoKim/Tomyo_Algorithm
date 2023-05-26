def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            last = stk[-1]
            if len(stk) != 0 and last < arr[i]:
                stk.append(arr[i])
                i += 1
            elif len(stk) != 0 and last >= arr[i]:
                stk.pop()
    
    return stk