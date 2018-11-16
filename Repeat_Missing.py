def repeatedNumber(self, a):
        sum,q,w,e,r=0,0,0,0,0
        
        A=[]
        n=len(a)
        
        for i in range(n):
            w += a[i]
            r += a[i]**2
            
        for i in range(n+1):    
            q += i
            e += i**2

        summ = (e-r) / (q-w)
        diff = (q-w)
        
        A.append(int( (summ-diff)/2 ))
        A.append(int( (summ+diff)/2 ))
       
        return A
