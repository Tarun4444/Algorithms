import sys
def min_diff(a,number):
    i=0
    j=len(a)-1
    diff=sys.maxsize

    while(j>i):
        if abs(a[i]*a[j]-number) < diff:
            diff=a[i]*a[j]-number
            r_i=i
            r_j=j

        if a[i]*a[j] > number:
            i+=1
        
        else:
            j-=1
        
    print(a[r_i],a[r_j])



        