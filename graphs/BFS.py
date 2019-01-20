from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def bfs(self,v):
        visited=[False]*len(self.graph)
        visited[v]=True
        q=[]
        q.append(v)
        while q:
            for i in self.graph[q[0]]:
                if(visited[i]!=True):
                    q.append(i)
                    visited[i]=True
            print(q[0])
            q.pop(0)
g=Graph()
g.add(0, 1)
g.add(0, 2)
g.add(1, 2)
g.add(2, 0)
g.add(2, 3)
g.add(3, 3)
g.bfs(2)
