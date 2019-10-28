def isSafe(x, y, m, n, maze, visited):
    if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or maze[x][y]=='#':
        return False
    return True

def printPathUtil(sx, sy, dx, dy, m, n, maze, possiblePaths, path, visited):
    if sx < 0 or sx >= m or sy < 0 or sy >= n or visited[sx][sy] or maze[sx][sy]=='#':
        return 

    if sx == dx and sy == dy:
        possiblePaths.append("".join(path))
        return 
    
    visited[sx][sy] = True

    if isSafe(sx+1, sy, m, n, maze, visited):
        path.append('D')
        printPathUtil(sx+1, sy, dx, dy, m, n, maze, possiblePaths, path, visited)
        path.pop()

    if isSafe(sx, sy-1, m, n, maze, visited):
        path.append('L')
        printPathUtil(sx, sy-1, dx, dy, m, n, maze, possiblePaths, path, visited)
        path.pop()

    if isSafe(sx, sy+1, m, n, maze, visited):
        path.append('R')
        printPathUtil(sx, sy+1, dx, dy, m, n, maze, possiblePaths, path, visited)
        path.pop()

    if isSafe(sx-1, sy, m, n, maze, visited):
        path.append('U')
        printPathUtil(sx-1, sy, dx, dy, m, n, maze, possiblePaths, path, visited)
        path.pop()

    visited[sx][sy] = False 

    
def printPath(sx, sy, dx, dy, m, n, maze):
    possiblePaths = []
    path = []
    visited = [[False for i in range(n)] for j in range(m)]
    printPathUtil(sx-1, sy-1, dx-1, dy-1, m, n, maze, possiblePaths, path, visited)
    if possiblePaths:
        x = sorted(possiblePaths, key=lambda x: (len(x),x))
        print(x[0])
    else:
        print('Impossible')

if __name__ == "__main__":
    inp = list(map(int,input().split()))
    m, n = inp[0], inp[1]
    maze = [[j for j in input().strip()] for i in range(n)] 
    q = int(input())
    for i in range(q):
        inp = list(map(int,input().split()))
        sx, sy, dx, dy = inp[0], inp[1], inp[2], inp[3]
        printPath(sx, sy, dx, dy, m, n, maze)