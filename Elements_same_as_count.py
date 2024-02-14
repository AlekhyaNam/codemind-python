n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if(a.count(i)==i):
        if i not in l:
            l.append(i)
if(len(l)==0):
    print(-1)
else:
    print(*l)
        