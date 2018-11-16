def isPalindrome(A):
    if A < 0:
        return 0
        
    def reverse(n):
        res = 0
        while n!=0:
            temp = n % 10
            res = res*10 + temp
            n //= 10

        print(res)    
        return res
    
    if A == reverse(A):print(1) 
    else:print(0)

isPalindrome(2147447412)
