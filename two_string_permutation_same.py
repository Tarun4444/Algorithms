def permutation(s1,s2):
    if len(s1)!=len(s2):
        return false

    d={}
    
    for c in s1 :
        if c in d:
            d[c]+=1
        else :
            d[c]=1

    for c in s2 :
        if c in d:
            if d.get(c)!=0 :
                d[c]-=1
            else:
                return false
        else :
            return false

    for i in range(len(d)):
        if d[c]!= 0
            return false
        
    return true
