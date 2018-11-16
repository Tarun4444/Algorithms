from collections import defaultdict
class Graph:
    def __init__(self,vertex):
        self.v = vertex
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)
        
    def topologicalSort(self):
        visited=[False]*self.v
        stack=[]

        for i in range(self.v):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        print (stack)

g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSort()
 
