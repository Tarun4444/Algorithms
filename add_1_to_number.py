def add():
    
    l=[9,9,9,9,9,9,9,9]
    n=len(l)
    carry=0
    
    sum=l[n-1]+1
    if sum > 9:
        carry=sum / 10
    else:
        carry = 0
    
    l[n-1]=sum % 10
    
    print(sum,carry,l)
    

    for i in range(n-1):
        sum=l[n-2-i]+carry
        if sum > 9:
            if n-2-i == 0:
                if sum > 9:
                    carry=sum/10
                    l[n-2-i]=int(sum%10)
                    l.insert(0,int(carry))
                else:
                    l[n-2-i]=int(sum)
                    carry=0
            else:
                carry = sum / 10
                l[n-2-i] = int(sum%10) 
        else:
            l[n-2-i]=int(sum)
            carry=0
            
            
        
    print(l)
    
    
add()