def count(m,n):
    
    a=[[0 for x in range(n)]for y in range(m)]
    a[0][0]=1
    
    #print(a)
    for i in range(1,n):
        a[0][i]=1
    
    #print(a)
    for j in range(1,m):
        a[j][0]=1
    
    
    #print(a)
    
    for i in range(1,m):
        for j in range(1,n):
            a[i][j]=a[i][j-1]+a[i-1][j]
    return a[m-1][n-1]

def sutta():
    t=int(input())
    for k in range(t):
        m,n = map(int,input().strip().split(" "))
        print(count(m,n)%1000000007)

sutta()
