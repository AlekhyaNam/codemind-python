n,m=map(int,input().split())
mat=[]
s=0
for i in range(n):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
    for j in range(m):
        s=s+mat[i][j]
print(s)
        
