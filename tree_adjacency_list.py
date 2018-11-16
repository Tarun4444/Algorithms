a={}
for i in range(10):
    x,y=map(int,input().split(" "))
    if x in a:
        if y not in a[x]:
            a[x].append(y)
    else:
        a[x]=[]
        a[x].append(y)
