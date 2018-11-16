#code
def sort_wave(a):
    n=len(a)
    for i in range(0,n,2):
        if i>0 and a[i-1]>a[i]:
            a[i],a[i-1]=a[i-1],a[i]
        if i<n-1 and a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            
    for i in range(n):
        print(a[i],end=" ")
    
t=int(input())
while t>0:
    a=[]
    n=int(input())
    a=list(map(int,input().split(" ")))
    sort_wave(a)
    t-=1
