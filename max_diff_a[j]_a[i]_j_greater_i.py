def boo(a):
    n=len(a)
    i,j=0,n-1
    k=0
    minn,maxx=float('+inf'),float('-inf')
    max_index,min_index =n,-1
    while max_index > min_index and k < n:
        if a[j] > maxx and j>=0 and j>min_index: 
            maxx=a[j]
            max_index=j

        if a[i]<minn and i < n and i<max_index:
            minn = a[i]
            min_index=i

        i+=1
        j-=1
        k+=1
        
    if max_index==n or min_index==-1:
        return -1
    return (a[max_index]-a[min_index])

a=[9,8,7,6,5,4,3]
print(boo(a))
