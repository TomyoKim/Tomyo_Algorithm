n=int(input())
N=n
count=0

while True:
    a=N//10
    b=N%10
    c=(a+b)%10
    N=(b*10)+c

    count+=1

    if(N==n):
        break

print(count)