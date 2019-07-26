#code
def to_input(a, m):
    x = [a[i:i+m] for i in range(0, len(a), m)]
    return x

def nge(a, n):
    b = []
    if len(a) < 0:
        return -1
    b.insert(0, (a[0],0))
    for i in range(1,n):
        if a[i] > b[0]:
            while len(b) > 0 and a[i] > b[0]:
                b.pop(0)
                print(a[i], end=" ")
            b.insert(0, (a[i], i))
        else:
            b.insert(0, (a[i], i))
    for i in range(len(b)):
        print(-1, end=" ")
        b.pop(0)

t=int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    nge(a,n)
    print()
    t = t - 1