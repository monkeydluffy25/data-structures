from collections import defaultdict
"""
class node():
    def __init__(self,data):
        self.vertex=data
        self.next=None
"""
class Graph:
    """
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*V
    def add(self,u,v):
        cur=node(v)
        cur.next=self.graph[u]
        self.graph[u]=cur
        cur=node(u)
        cur.next=self.graph[v]
        self.graph[v]=cur
    def print(self):
        for i in range(self.V):
            print(i)
            cur=self.graph[i]
            while cur:
                print(cur.vertex)
                cur=cur.next
            print()    
    """
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def dfs(self,v,visited):
        visited[v]=True
        print(v)
        for i in self.graph[v]:
            if (visited[i]!=True):
                self.dfs(i,visited)
    def start(self,v):
        visited=[False]*len(self.graph)
        self.dfs(v,visited)
g=Graph()
g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(2,0)
g.add(2,3)
g.add(3,3)
g.start(2)
