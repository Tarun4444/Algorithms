def gcd(a, b):
    if a==0 or b==0:
        return 0
    if a==b :
        return a
    if a > b :
        return gcd(a-b,b)
    else :
        return gcd(a,b-a)

print(gcd(4,6))
