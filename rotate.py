#code
def rotate(a, n, k):
    x = a[-1]
    a.insert(0, x)
    a.pop(-1)
    a.pop(n-k)
    
t=int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    for k in range(n-1):
        rotate(a, n, k+1)
    print(a[0])
    t = t - 1