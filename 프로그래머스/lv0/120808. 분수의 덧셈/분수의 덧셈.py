import math

def solution(numer1, denom1, numer2, denom2):
    number = denom1*numer2 + denom2*numer1
    denom = denom1*denom2
    gcd = math.gcd(denom, number)
    answer = [number//gcd, denom//gcd]
    return answer