t=int(input())
while t > 0:
    n,x,y=map(int,input().split(" "))
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    
    tip=0
    for i in range(n):
        if a[i] > b[i]:
            tip+=a[i]
        else:
            tip+=b[i]
    
    print(tip)
    t-=1
