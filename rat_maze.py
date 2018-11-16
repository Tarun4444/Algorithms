def sol(B):
    s=""
    for i in B:
        for j in B:
            if B[i][j]==1:
                s+=str(j)+" "+str(i)
    print(s)

def checkRange(A,x,y):
    if x > 0 and y > 0 and x < n-1 and y < n-1 and A[x][y]==1 :
        return true
    return false

def solveMaxe(A):
    B=[[0 for j in range(4)] for i in range(4)]
    if rat(A,0,0,B) == True :
        sol(B)
        return True
    return False

def rat(A,x,y,B):
    if x == n-1 or y == n-1:
        B[x][y]=1
        return true

    if checkRange(A,x,y) == True:
        B[x][y]=1
        if rat(A,x+1,y,B) == True:
            B[x+1][y] = 1
        if rat(A,x,y+1,B) == True:
            B[x][y+1] = 1

        B[x][y]=0        
        return false
