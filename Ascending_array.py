n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n-1):
    if(l[i]<l[i+1]):
        c=c+1
if(c==n-1):
    print("yes")
else:
    print("no")