n=int(input())
arr=list(map(int,input().split()))
m=int(input())
l=[]
for i in arr:
    if(arr.count(i)==m):
        if i not in l:
            l.append(i)
if(len(l)>0):
    print(*l)
else:
    print(-1)