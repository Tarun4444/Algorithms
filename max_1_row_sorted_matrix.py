def binary_search(A, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if mid == 0 and A[0] == 1:
        return 0
    if A[mid] == 1 and A[mid-1] == 0:
        return mid
    if A[mid] == 0:
        return binary_search(A, mid+1, high)
    if A[mid-1] == 1:
        return binary_search(A, low, mid-1)
    

def max_one(matrix, m, n):
    max_row_index = -1
    for i in range(m):
        if matrix[i][n-1] != 0:
            a = binary_search(matrix[i], 0, n-1)
        else:
            a = n
        if n - a > max_row_index :
            max_row_index = i
    return max_row_index

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

t = int(input())
while t > 0:
    m, n = map(int, input().split(" "))
    mat = list(map(int, input().split()))
    mat = to_matrix(mat, n)
    print(max_one(mat, m, n))
    t = t - 1