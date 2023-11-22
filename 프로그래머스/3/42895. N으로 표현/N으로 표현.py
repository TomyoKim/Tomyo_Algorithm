def solution(N, number):
    dp = []
    
    for i in range(1, 9):
        case = {int(str(N) * i)}
        
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    case.add(x+y)
                    case.add(x-y)
                    case.add(x*y)
                    if y != 0:
                        case.add(x//y)
        if number in case:
            return i
        dp.append(case)
    return -1