def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
n=int(input())
n=n+1
while(n>0):
    if(prime(n)==1):
        if(str(n)==str(n)[::-1]):
            print(n)
            break
    n=n+1