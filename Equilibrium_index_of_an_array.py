t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(0,len(a)):
        l=a[0:i+1]
        ll=a[i:len(a)]
        if(sum(l)==sum(ll)):
            print(i)
            break
    else:
        print(-1)