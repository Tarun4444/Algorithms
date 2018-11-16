def search(a,low,high):
    if low > high:
        return -1
    
    mid = (low + high)//2
    if (mid==0 or a[mid-1]==0) and a[mid]==1:
        return mid
    elif a[mid]==0:
        return search(a,mid+1,high)
    else:
        return search(a,low,mid-1)
    
def boo(arr,m,n):
    maxx=-1
    max_row_index=0
    for i in range(m):
        index = search(arr[i],0,n-1)
        if index != -1 and n-index > maxx:
            maxx = n-index
            max_row_index = i
    print(max_row_index)

t=int(input())
while t:
    m,n=map(int,input().split(" "))
    a=list(map(int,input().split(" ")))
    arr=[[0 for i in range(n)] for i in range(m)]
    k=0
    for i in range(m):
        for j in range(n):
            arr[i][j]=a[k]
            k+=1
    
    boo(arr,m,n)
    t-=1
