a=[9,6,4,2,3,8]
b=[1,2,8,6,2]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=[]
for i in b:
    if i in d :
        if d[i] > 0:
            l.append(i)
        d[i]-=1
l.sort()
print(l)

    
