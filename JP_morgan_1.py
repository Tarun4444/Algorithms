import math 

def pF(n):
    z = []
    while n % 2 == 0: 
        z.append(2) 
        n = n / 2
    
    i = 3  
    while i <= int(math.sqrt(n)):
        while n % i== 0: 
            z.append(i) 
            n = n / i 
        i+=2

    if n > 2: 
        z.append(n) 
    
    if not z:
        print(-1)
    else:
        z.sort()
        print(z[0])

def gcd(a,b): 
    if (b == 0): 
        return a 
    return gcd(b, a%b) 


inp = list(map(int,input().split()))
m, n = inp[0], inp[1]

r1 = gcd(m, n)
pF(r1)
