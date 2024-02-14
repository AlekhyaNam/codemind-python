n=int(input())
l=list(map(int,input().split()))
ll=[]
c=0
for i in l:
    if(l.count(i)==i):
        if i not in ll:
            ll.append(i)
            c=c+1
if(len(ll)!=0):
    print("%0.2f"%(sum(ll)/c))
else:
    print(-1)