from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.l = defaultdict(list)
    
    def add_edge(self, u, v):
        self.l[u].append(v)
        # self.l[v].append(u)
        
    def topological_sort(self, visited, i, sac):
        visited[i] = 1
        for j in self.l[i]:  
            if visited[j] == 0:
                self.topological_sort(visited, j, sac)
        sac.append(i)
    
    def topological_sort_util(self, n, k):
        visited = [0 for i in range(k)]
        sac = []
        for i in range(k):
            if visited[i] == 0:
                self.topological_sort(visited, i, sac)
        b = []
        for q in sac:
            b.append(chr(ord('a') + q))
        print(''.join(b[::-1]))

    def print_sorted_words(self, words, n, k):
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            l = min(len(first), len(second))
            for j in range(l):
                if first[j] != second[j]:
                    self.add_edge(ord(first[j])-ord('a'), ord(second[j])-ord('a'))
                    break
        self.topological_sort_util(n, k)

if __name__ == '__main__':
    t = int(input())
    words = []
    while t > 0:
        inp = list(map(int,input().split()))
        n, k = inp[0], inp[1]
        words = list(input().split())
        g = Graph(k)
        g.print_sorted_words(words, n, k)
        t = t - 1

