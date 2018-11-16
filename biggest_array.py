from functools import cmp_to_key

def largestNumber(A):
    A = map(str, A)
    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
    res = ''.join(sorted(A, key= key, reverse=True))
    res = res.lstrip('0')
    return res if res else '0'
        
A=[]
largestNumber()