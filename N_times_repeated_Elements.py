n=int(input())
l=list(map(int,input().split()))
k=int(input())
ll=[]
for i in l:
    if(l.count(i)==k and i not in ll):
        ll.append(i)
if(len(ll)==0):
    print(-1)
else:
    print(*ll)