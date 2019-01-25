from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def dfs(self,u,visited):
        visited[u]=True
        for i in self.graph[u]:
            if(visited[i]!=True):
                self.dfs(i,visited)
    def mother(self):
        visited=[False]*(self.V)
        for i in range(self.V):
            if(visited[i]!=True):
                self.dfs(i,visited)
                v=i
        return v
g=Graph(7)
g.add(0, 1)
g.add(0, 2)
g.add(1, 3)
g.add(4, 1)
g.add(6, 4)
g.add(5, 6)
g.add(5, 2)
g.add(6, 0)
print(g.mother())
