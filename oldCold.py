def old_cold_number(x):
    c=0
    for i in range(1,x):
        if i%2 != 0:
            c+=1
        
    if x%c == 0:
        return "Old number"
    
    return "Cold number"
    
    
def subarray(a,n,l,r):
    old_count=cold_count=0
    b=[0]*n
    
    for number in range(l,r+1):
        if old_cold_number(a[number-1])=="Old number":
            old_count+=1 

        if old_cold_number(a[number-1])=="Cold number":
            cold_count+=1
            b[number-1]=1

    if old_count >= cold_count:
        return 0
    elif:
        for number in range(l,r+1):
            
            
            
    
a=[]
l=[]
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    for j in range(q):
        l=list(map(int,input().split()))
        print(subarray(a,n,l[0],l[1]))
        