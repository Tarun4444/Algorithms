def nearest_multiple(n):
    if n < 10:
        if n <= 5:
            return 0
        return 10
    rem = n%10
    if rem <= 5:
        n = n-rem
    else :
        n = n + (10-rem)
    return n

t=int(input())
while t > 0:
    n= int(input())
    print(nearest_multiple(n))
    t-=1
