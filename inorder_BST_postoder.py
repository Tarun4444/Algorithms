def preorder(a,low,high):
    n=len(a)
    if low > high:
        return
    mid=int((low+high)/2)
        
    print(a[mid],end=" ")
    preorder(a,low,mid-1)
    preorder(a,mid+1,high)

t=int(input())
while t>0:
    a=[]
    n=int(input())
    try:
        a = [int(x) for x in input().split(" ")] 
    except ValueError:
        pass
    preorder(a,0,n-1)
    t-=1
