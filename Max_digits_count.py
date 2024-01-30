n=int(input())
arr=list(map(int,input().split()))
m=0
for i in arr:
    m=max(m,len(str(i)))
c=0
for i in arr:
    if(len(str(i))==m):
        c=c+1
print(c)