n=int(input())
m=100000007
arr=list(map(int,input().split()))
for i in arr:
    m=min(len(str(i)),m)
c=0
for i in arr:
    if(len(str(i))==m):
        c=c+1
print(c)