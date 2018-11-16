def product(arr,n):
    curr_prod,max_prod=1,0
    min_prod=1
    
    for i in range(n):
        if arr[i] != 0:
            curr_prod=curr_prod * arr[i]
            min_prod = min_prod*arr[i]
            if curr_prod < 0:
                curr_prod = 1
            if min_prod > curr_prod:
                curr_prod=min_prod
        else:
            curr_prod = 1
            min_prod  = 1
        
        if curr_prod > max_prod:
            max_prod = curr_prod
            
    print(max_prod)

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int , input().split()))
    product(arr,n)