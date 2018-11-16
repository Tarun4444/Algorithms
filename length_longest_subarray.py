
def length_longest_subarray(arr,n):
    current_count,max_count=0,0
    for i in range(n):
        if arr[i]>=0:
            current_count+=1
        else:
            current_count = 0
        
        if max_count < current_count :
            max_count=current_count

    print(max_count)
    
t=int(input())
arr=[]
for i in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    length_longest_subarray(arr,n)