def preOrder(a, l, r, alpha):
    if l >= n or r > n or l>r:
        return  
    if l == r :
        alpha.append(a[l])
        return 
    root = (l + r) // 2 
    alpha.append(a[root])
    preOrder(A, l, root-1, alpha)
    preOrder(A, root+1, r, alpha)

    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        alpha = []
        A = list((input().split(" ")))
        preOrder(A, 0, n, alpha)
        print(" ".join(alpha))
        t = t - 1