#code
def to_input(a, m):
    x = [a[i:i+m] for i in range(0, len(a), m)]
    return x

def knapsack(w, weights, values, i):
    if i == 0 or w == 0:
        return 0
    if weights[i] < w:
        return knapsack(w, weights, values, i-1)
    else:
        return max(values[i-1] + knapsack(w - weights[i-1], weights, values, i-1), knapsack(w , weights, values, i-1))

def knapsack_dp(w, wt, val, n):
    if w == 0 or n == 0:
        return 0
    k = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                k[i][j] == 0
            if j >= wt[i-1]:
                k[i][j] = max(val[i-1] + k[i-1][j-wt[i-1]], k[i-1][j])
            else:
                k[i][j] = k[i-1][j]
    return k[n][w]

t=int(input())
while t > 0:
    n = int(input())
    W = int(input())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    
    if len(weights) == 0 or len(values)==0 or W == 0 or sum(weights) == 0:
         print(0)
         continue
    print(knapsack_dp(W, weights, values, n))
    # print(knapsack(W, weights, values, n))
    t = t - 1