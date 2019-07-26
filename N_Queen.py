#code
def isSafe(board, row, col):
    N = len(board)
    curr_row = row
    curr_col = col
    while curr_col >= 0:
        while curr_row >= 0:
            if board[curr_row][curr_col] == 1:
                return False
            
            if board[curr_row-1][curr_col-1]==1:
                return False
            
            if board[curr_row+1][curr_col-1]==1:
                return False
                
            curr_row = curr_row - 1
        curr_col = curr_col - 1
    return True
    

def solveNQUtil(board, col, N):
    
    if col>=N:
        return True
    
    for i in range(col, N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col+1, N):
                return True
            board[i][col] = 0
    
    return False
        
t = int(input())
while t > 0:
    n = int(input())
    board = [[0]*n for i in range(n)]
    
    if solveNQUtil(board, 1, N) == False:
        print(-1)
    else :
        print(1)
    
    t = t - 1
    