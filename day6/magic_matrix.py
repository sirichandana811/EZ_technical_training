n=int(input())
m=[[0]*n for i in range(n)]
k=1
i=n//2
j=n-1
while(k<=n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if m[i][j]:
        i=i+1
        j=j-2
        continue
    m[i][j]=k
    k+=1
    i=i-1
    j=j+1
for i in m:
    print(*i)
print('magic matrix =',n*((n*n)+1)//2)
    
