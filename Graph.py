# Graph 
#   Intro to Graph 
#   Graph representation (Adjacence Matrix)
#   Graph representation (Adjacence List)
#   Graph adjacency list representation in Python 
#   Adjacency Matrix and List Comparison 
#   Breadth First Search in Python 
#   BFS for disconnected graph 
#   Connected Components in an undirected graph using BFS 
#   Applications of BFS 
#   Depth First Search 
#   DFS for Disconnected Graph 
#   Connected components in an undirected graph using DFS 
#   Applications of DFS 
#   Shortest path in an unweighted graph 
#   Detect cycle in undirected graph 
#   Detect cycle in a directed graph 
#   Topological sorting (Kahn's BFS Based algorithm)
#   Topological sorting (DFS based algorithm) 
#   Shortest path in DAG 
#   Prim's algorithm/Minimum spanning tree 
#   Implementation of Prims algorithm 
#   Dijkstra's Shortest path algorithm 
#   Kosaraju's algorithm 
#   Bellman Ford Shortest Path algorithm 
#   Articulation Point 
#   Bridges in Graph 
#   Tarjans algorithm 
#   Kruskal's algorithm 


## Graph adjacency list representation in Python  
def addEdge(adj, u, v) : 
    adj[u].append(v)
    adj[v].append(u) 
def printGraph(adj) : 
    for l in adj : 
        print(l, end=" ")
V=4 
adj=[[] for i in range(V)] 
addEdge(adj, 0, 1)
addEdge(adj, 0, 2)
addEdge(adj, 1, 2)
addEdge(adj, 1, 3)
print("Graph adjacency list representation : ", end=" ")
printGraph(adj)
print("\n")


## Breadth First Search in Python 
from collections import deque 
def BFS(adj, s) : 
    visited=[False]*len(adj) 
    q=deque() 
    q.append(s) 
    visited[s]=True 
    while q : 
        s=q.popleft() 
        print(s, end=" ") 
        for u in adj[s] : 
            if visited[u]==False : 
                q.append(u) 
                visited[u]=True 
adj=[[1,2], [0,2,3], [0,1,3,4], [1,2,4], [2,3]] 
print("BFS (first version) : ", end=" ")
BFS(adj, 0)
print("\n") 


## BFS for disconnected graph
def BFS(adj, s, visited) : 
    q=deque() 
    q.append(s) 
    visited[s]=True 
    while q : 
        s=q.popleft() 
        print(s, end=" ")
        for u in adj[s] : 
            if visited[u]==False : 
                q.append(u) 
                visited[u]=True 
def BFSDis(adj) : 
    visited=[False]*len(adj) 
    for u in range(len(adj)) : 
        if visited[u]==False : 
            BFS(adj, u, visited) 
adj=[[1,2], [0,3], [0,3], [1,2], [5,6], [4,6] ,[4,5]]
print("BFS for disconnected graph")
BFSDis(adj)
print("\n") 


## Connected Components in an undirected graph using BFS 
def BFS(adj, s, visited) : 
    q=deque() 
    q.append(s) 
    visited[s]=True
    while q : 
        s=q.popleft() 
        for u in adj[s] : 
            if visited[u]==False : 
                q.append(u) 
                visited[u]=True 
def BFSConnect(adj) : 
    visited=[False]*len(adj)
    res=0  
    for u in range(len(adj)) : 
        if visited[u]==False : 
            res+=1 
            BFS(adj, u, visited) 
    return res 
print("Connected Components in an undirected graph using BFS ")
adj=[[1,2], [0,2], [0,1], [4], [3], [6,7], [5], [5]]
print(BFSConnect(adj))

adj=[[1,2], [2], [1]]
print(BFSConnect(adj))
print("\n") 


## Depth First Search 
def DFSrec(adj, s, visited) : 
    visited[s]=True 
    print(s, end=" ") 
    for u in adj[s] : 
        if visited[u]==False : 
            DFSrec(adj, u, visited) 
def DFS(adj, s) :  
    visited=[False]*len(adj) 
    DFSrec(adj, s, visited)
adj=[[1,4], [0,2], [1,3], [2], [0,5,6], [4,6], [4,5]]
s=0 
print("Depth First Search (DFS) ")
DFS(adj, s) 
print()
adj=[[1,2], [0,3,4], [0,3], [1,2], [1,5], [4]]
s=0 
DFS(adj, s)
print("\n")


## DFS for Disconnected Graph
def DFSrec(adj, s, visited) : 
    visited[s]=True 
    print(s, end=" ")
    for u in adj[s] : 
        if visited[u]==False : 
            DFSrec(adj, u, visited) 
def disconDFS(adj) :
    visited=[False]*len(adj)
    for u in range(len(adj)) : 
        if visited[u]==False : 
            DFSrec(adj, u, visited)
adj=[[1,2], [0,2], [0,1], [4], [3]] 
print("DFS for disconnected graph ")
disconDFS(adj)
print()
adj=[[1,2], [0,2,3], [0,1], [1,4], [3]]
disconDFS(adj)
print() 
adj=[[1,3], [0,3,2], [1,4], [0,1], [2]]
disconDFS(adj)
print("\n")


## Connected Components in an undirected graph using BFS 
def DFSrec(adj, s, visited) : 
    visited[s]=True 
    for u in adj[s] : 
        if visited[u]==False : 
            DFSrec(adj, u, visited) 
def DFScon(adj) : 
    visited=[False]*len(adj) 
    res=0 
    for u in range(len(adj)) : 
        if visited[u]==False : 
            res+=1 
            DFSrec(adj, u, visited) 
    return res
adj=[[1,2], [0,2], [0,1], [4], [3]]
print("Connected comp in undirected graph : ",DFScon(adj))
print("\n")


## Shortest path in an unweighted graph 
from collections import deque 
INT_MAX=float("inf")

def BFS(adj, s, dist) : 
    visited=[False]*len(adj) 
    q=deque() 
    dist[s]=0
    visited[s]=True 
    q.append(s) 
    while q : 
        u=q.popleft() 
        for v in adj[u] : 
            if visited[v]==False : 
                dist[v]=dist[u]+1 
                visited[v]=True 
                q.append(v) 
adj=[[1,2], [0,2,3], [0,1,3], [1,2]]
dist=[INT_MAX]*len(adj)
BFS(adj, 0, dist)
print("Shortest path in undirected graph : ",dist)
print("\n")


## Detect cycle in undirected graph 
def DFSrec(adj, s, visited, parent) : 
    visited[s]=True 
    for u in adj[s] : 
        if visited[u]==False : 
            if DFSrec(adj, u, visited, s) : 
                return True 
        elif u!=parent : 
            return True 
    return False 
def DFS(adj) : 
    visited=[False]*len(adj)
    for i in range(len(adj)) : 
        if visited[i]==False : 
            if DFSrec(adj, i, visited, -1) : 
                return True 
    return False 
adj=[[1], [0,2,3], [1,3,4], [1,2], [2]]
print("Detect cycle in undirected graph : ",DFS(adj)) 
print("\n") 


## Detect cycle in a directed graph
def DFSrec(adj, s, visited, recSt) : 
    visited[s]=True 
    recSt[s]=True 
    for u in adj[s] : 
        if visited[u]==False and DFSrec(adj, u, visited, recSt) : 
            return True 
        elif recSt[u]==True : 
            return True 
    recSt[s]=False 
    return False 
def DFS(adj) : 
    visited=[False]*len(adj)
    recSt=[False]*len(adj) 
    for i in range(len(adj)) : 
        if visited[i]==False : 
            if DFSrec(adj, i, visited, recSt) : 
                return True 
    return False 

print("Detect cycle in directed graph ")
adj=[[1], [], [1,3], [4], [5], [3]]
if DFS(adj) : 
    print("Cycle found")
else : 
    print("No Cycle found") 

adj=[[1], [2], [3], [1]]
if DFS(adj) : 
    print("Cycle found")
else : 
    print("No Cycle found") 

adj=[[1], [3], [1,3], []]
if DFS(adj) : 
    print("Cycle found")
else : 
    print("No Cycle found") 
print("\n")


## Topological sorting (Kahn's BFS Based algorithm)
from collections import defaultdict
def topologicalSort(adj):
    V=len(adj)		 
    in_degree = [0]*V 
    for i in range(len(adj)) :
    	for j in adj[i]:
    		in_degree[j] += 1
    queue = []
    for i in range(V):
    	if in_degree[i] == 0:
    		queue.append(i)
    cnt = 0
    top_order = []
    while queue:
    	u = queue.pop(0)
    	top_order.append(u)
    	for i in adj[u]:
    		in_degree[i] -= 1
    		if in_degree[i] == 0:
    			queue.append(i)
    	cnt += 1
    if cnt != V:
    	print ("There exists a cycle in the graph")
    else :
    	print(top_order)
print("Topological Sorting ")
adj=[[1,2], [3], [3], [4,5], [], []]
topologicalSort(adj)
adj=[[2,3], [3,4], [], [], []]
topologicalSort(adj)
print("\n")



## Detect cycle using Kahn's 
def DetectCycleKahns(adj) : 
    V=len(adj) 
    indegree=[0]*V 
    for u in range(V) : 
        for x in adj[u] : 
            indegree[x]+=1 
    q=deque() 
    for i in range(V) : 
        if indegree[i]==0 : 
            q.append(i) 
    count=0 
    while q : 
        u=q.popleft() 
        for x in adj[u] : 
            indegree[x]-=1 
            if indegree[x]==0 : 
                q.append(x)
        count+=1 
    if count!=V : 
        print("Cycle exists")
    else : 
        print("No Cycle exists")
print("Detect Cycle using Kahn's Algorithm ")
adj=[[1], [2], [], [1], [1]]
DetectCycleKahns(adj)
adj=[[1], [2], [3], [1]]
DetectCycleKahns(adj)
print("\n") 


## Topological sorting (DFS based algorithm)
def topologicalSortUtil(adj, v, visited, stack):
	visited[v] = True
	for i in adj[v]:
		if visited[i] == False:
			topologicalSortUtil(adj, i, visited, stack)
	stack.append(v)

def topologicalSort(adj): 
    V=len(adj)
    visited = [False]*V
    stack = []
    for i in range(V):
    	if visited[i] == False:
    		topologicalSortUtil(adj, i, visited, stack)
    print(stack[::-1]) 
print("Topological sorting (DFS based)")
adj=[[1], [3], [3,4], [4], []]
topologicalSort(adj)
print("\n")


## Shortest path in DAG 
# Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity :O(V+E)

from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.V = vertices 
		self.graph = defaultdict(list)
            
	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))
    
	def topologicalSortUtil(self,v,visited,stack):
		visited[v] = True
		if v in self.graph.keys():
			for node,weight in self.graph[v]:
				if visited[node] == False:
					self.topologicalSortUtil(node,visited,stack)
		stack.append(v)

	def shortestPath(self, s):
		visited = [False]*self.V
		stack =[]
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(s,visited,stack)
		dist = [float("Inf")] * (self.V)
		dist[s] = 0
		while stack:
			i = stack.pop()
			for node,weight in self.graph[i]:
				if dist[node] > dist[i] + weight:
					dist[node] = dist[i] + weight
		for i in range(self.V):
			print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")

g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
s = 1
print ("Following are shortest distances from source %d " % s)
g.shortestPath(s)
print("\n")



# Shortest path in DAG (Code-2)
def topologicalSortUtil(adj,v,visited,stack):
	visited[v] = True
	if v in adj.keys() :
		for node,weight in adj[v]:
			if visited[node] == False:
				topologicalSortUtil(adj,node,visited,stack)
	stack.append(v)

def shortestPath(adj, s) :
    V=len(adj)
    visited = [False]*V
    stack =[]
    for i in range(V):
    	if visited[i] == False:
    		topologicalSortUtil(adj,s,visited,stack)
    dist = [float("Inf")] * V
    dist[s] = 0
    while stack:
    	i = stack.pop()
    	for node,weight in adj[i] :
    		if dist[node] > dist[i] + weight :
    			dist[node] = dist[i] + weight
    for i in range(V):
    	print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")

adj=defaultdict(list)
adj[0]=[(1,5), (2,3)] 
adj[1]=[(2,2), (3,6)]
adj[2]=[(3,7), (4,4), (5,2)] 
adj[3]=[(4,-1)]
adj[4]=[(5,-2)]
adj[5]=[]
print ("Following are shortest distances from source %d " % s)
s=1
shortestPath(adj, s)
print("\n")


## Prim's Algorithm / Minimum Spanning Tree  
def primMST(graph) :  
    V=len(graph) 
    key=[float("inf") for i in range(V)] 
    key[0]=0 
    res=0 
    mSet=[False for i in range(V)] 
    for count in range(V) : 
        u=-1 
        for i in range(V) :
            if mSet[i]==False and (u==-1 or key[i]<key[u]) : 
                u=i 
        mSet[u]=True 
        res+=key[u] 
        for v in range(V) :  
            if mSet[v]==False and graph[u][v]!=0 and graph[u][v]<key[v] : 
                key[v]=graph[u][v]
    return res 
graph=[[0,2,0,6,0], [2,0,3,8,5], [0,3,0,0,7], [6,8,0,0,9], [0,5,7,9,0]] 
print("Prim's Algo (MST) : ",primMST(graph))
print("\n")


## Dijkstra's Shortest path algorithm
def dijkstra(graph, src) : 
    V=len(graph)
    dist=[float("inf") for i in range(V)] 
    dist[src]=0 
    fin=[False for i in range(V)] 
    for count in range(V-1) : 
        u=-1 
        for i in range(V) : 
            if fin[i]==False and (u==-1 or dist[i]<dist[u]) : 
                u=i 
        fin[u]=True 
        for v in range(V) : 
            if fin[v]==False and graph[u][v]!=0 : 
                dist[v]=min(dist[v], dist[u]+graph[u][v])
    return dist 
print("Dijkstra's Algorithm : ")
graph=[[0,5,10,0], [5,0,3,20], [10,3,0,2], [0,20,2,0]]
src=0 
print(dijkstra(graph, src))
graph=[[0,5,3], [5,0,1], [3,1,0]] 
src=1 
print(dijkstra(graph, src))
print("\n")


