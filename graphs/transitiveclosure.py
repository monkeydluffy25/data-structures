from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def dfs(self,s,u,arr):
        arr[s][u]=1
        for i in self.graph[u]:
            if(arr[s][i]!=1):
                self.dfs(s,i,arr)
    def calldfs(self):
        arr=[[0 for i in range(self.V)]for j in range(self.V)]
        for i in range(self.V):
            self.dfs(i,i,arr)
        print(arr)
g = Graph(4)
g.add(0, 1)
g.add(0, 2)
g.add(1, 2)
g.add(2, 0)
g.add(2, 3)
g.add(3, 3)
g.calldfs()
