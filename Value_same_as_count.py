n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in l:
    if(l.count(i)==i and i not in ll):
        ll.append(i)
print(len(ll))
        