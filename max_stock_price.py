#code
def to_input(a, m):
    x = [a[i:i+m] for i in range(0, len(a), m)]
    return x

def stock_buy_sell(A):
    for idx in range(len(A) - 1,0,-1):
        A[idx] = A[idx] - A[idx - 1]
    A[0] = -A[0]
    A = A + [-100]
    buy_sell = []
    for idx in range(1,len(A)):
        if (A[idx] > 0) and (A[idx-1] < 0):
            buy = idx-1
        if (A[idx] < 0) and (A[idx-1] > 0):
            sell = idx-1
            buy_sell.append((buy, sell))

    for a in buy_sell:
        print('('+str(a[0]),str(a[1])+')', end=' ')
    if not buy_sell:
        print('No Profit', end=' ')
        
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = [int(a) for a in input().split()]
        (stock_buy_sell(A))
        print()
        




# def max_day_stock(a, n):
    
#     if n == 1:
#         return "No Profit"
    
#     count = 0
#     i = 0
#     b = []
#     while i < n:
#         c= [0,0]
#         # buy
#         while i < n-1 and a[i] >= a[i+1]:
#             i += 1
        
#         if i == n-1:
#             break
        
#         c[0] = i
#         i+=1
        
#         # sell
#         while i < n and a[i] >= a[i-1]:
#             i += 1
        
#         c[1] = i-1
#         count = count + 1
        
#         b.append(c)
#     return b, count

# t=int(input())
# while t > 0:
#     n = int(input())
#     a = list(map(int, input().split()))
#     z, c_ = max_day_stock(a,n) 
#     if c_ == 0:
#         print("No Profit")
#     else:
#         i = 0
#         while i < c_:
#             print("(" + str(z[i][0]) + " " + str(z[i][1]) + ")", end=" ")
#             i+=1
#     print()
#     t = t - 1