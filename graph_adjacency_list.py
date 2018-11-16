def adjacency_list(A):
    l={}
    for a in A:
        if a[0] not in l:
            l[a[0]]=[a[1]]
        else:
            l[a[0]].append(a[1])
        if a[1] not in l:
            l[a[1]]=[a[0]]
        else:
            l[a[1]].append(a[0])
            
    for i in range(len(l)):
        print(i,end="-> ")
        x=1
        for a in l[i]:
            if x==len(l[i]):
                print(a,end="")
            else:
                print(a,end="-> ")
                x+=1
        print()
    
t=int(input())
while t>0:
    a=[]
    v,e = map(int,input().strip().split())
    for i in range(e):
        a.append(list(map(int,input().strip().split())))
    if e!=0:
        adjacency_list(a)
    else:
        for i in range(v):
            print(i)
    t-=1
    