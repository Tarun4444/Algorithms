
def tile(w):
    a = [0] * (w) 
    a[0] = 1
    a[1] = 2
    for i in range(2,w):
        a[i] = a[i-1] + a[i-2]
    return a[w-1]
    
t=int(input())
while t > 0:
    w = int(input())
    print(tile(w))
    t = t - 1