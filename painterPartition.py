def isValid(a,n,k,mid):
    students=1
    current_page=0

    for i in range(n):
        if current_page + a[i] > mid:
            students+=1
            if students > k:
                return False
        else:
            current_page+=a[i]
    
    return True

def binary_search(a,n,k):
    high=0
    low=0
    total_pages=0

    for i in range(n):
        total_pages+=a[i]

    low = a[n-1]
    high = total_pages

    if n < k:
        return 0
    
    if k==1:
        return high
    
    while(low < high):
        mid=(low+high)/2

        if(isValid(a,n,k,mid)):
            high=mid-1
            finalAns=mid
        else:
            low=mid+1

    return finalAns

def main():
    t=int(input())
    a=[]
    for i in range(t):
        n=int(input())
        k=int(input())
        a=list(map(int,input().split()))
        binary_search(a,n,k)

main()