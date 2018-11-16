t = int(input())
for k in range(t):
    n = int(input())
    a=[]
    a = input()

    a = a.split()
    i = 0
    j = i+1
    
    for i in range(n):
        c=0
        if i!=n-1:
            for j in range(i+1,n):
            
                if a[j] > a[i]:
                    c= 1
                    print(a[j],end=" ")
                    break
            if c == 0:
                print(-1,end=" ")
        else:
            print(-1,end=" ")
    print()
    t = t-1
