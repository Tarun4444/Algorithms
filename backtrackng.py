#code

class Graph:
    def __init__(self , vertices):
        self.V = vertices
        self.graph = [[0 for j in range(vertices)] for j in range(vertices)]
    
    def isSafe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] and color[i] == c:
                return False
        return True
    
    
    def graphColorUtil(self, m, color, v):
        if v == self.V:
            return True
        
        for c in range(1,m+1):
            if self.isSafe(v, color, c) == True:
                color[v] = c
                if self.graphColorUtil(m, color, v+1) == True:
                    return True
                color[v] = 0
    
    def graphColoring(self, m):
        color = [0]*self.V
        if self.graphColorUtil(m, color, 0) == None:
            return False
        return True

t=int(input())
while t > 0:
    n = int(input())
    m = int(input())
    g = int(input())
    pairs = list(map(int, input().split()))
    G = Graph(n)
    
    for i in range(0,len(pairs)-1,2):
        G.graph[pairs[i]-1][pairs[i+1]-1] = 1
        
    print(1) if G.graphColoring(m) else print(0)
    t = t - 1
