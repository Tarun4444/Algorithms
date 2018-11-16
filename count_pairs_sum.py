# cook your dish here

def pair_sum(arr,s):
    a=[[False for x in range((s+1))]for j in range(len(arr))+1]
    
    for x in range(len(arr)):
        a[x][0]=True
        
    #print(a)
    
    for i in range(1,len(arr)+1):
        for j in range(1,s+1):
            
            if j<arr[i-1]:
                a[i][j]=a[i-1][j]
        
            if j>=arr[i-1]:
                a[i][j]=a[i-1][j] or a[i-1][j-arr[i-1]]
            
            
            #print(a[i][j])

    print(a[len(arr)][s])
    
t=int(input())
arr=[]
for i in range(t):
    arr = list(map(int, input().split()))
    s=int(input())
    pair_sum(arr,s)