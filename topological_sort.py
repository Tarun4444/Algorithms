from collections import defaultdict

def toposort(visited, graph, i, a):
    visited[i] = True
    a.append(i)
    for j in range(len(graph[i])):
        if visited[graph[i][j]] == False:
            toposort(visited, graph, graph[i][j], a)
    return a

def topoSort(n, graph):
    # Code here
    visited = [False for i in range(n)]
    a = []
    for i in range(n):
        if visited[i] == False:
           toposort(visited, graph, i, a)
    return a

def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        print (res)
        valid=True
        for i in range(N):
            n = len(graph[res[i]])
            for j in range(len(graph[res[i]])):
                for k in range(i+1, N):
                    if res[k]==graph[res[i]][j]:
                        n-=1
            # print n
            if n!=0:
                valid=False
                break
        if valid:
            print(1)
        else:
            print(0)