from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfsUtil(self,v,visited):
        visited[v]=true
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfsUtil(i,visited)
                
    def dfs(self,v):
        visited = [False]*len(self.graph)
        for i in range(len(self.graph)):
            self.dfsUtil(i,visited)

    
        

    
    
