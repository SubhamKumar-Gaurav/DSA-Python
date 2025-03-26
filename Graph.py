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


## Kosaraju's Algorithm  
from collections import defaultdict

def dfs_util(adj, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in adj[v]:
        if not visited[i]:
            dfs_util(adj, i, visited)

def fill_order(adj, v, visited, stack):
    visited[v] = True
    for i in adj[v] :
        if not visited[i] :
            fill_order(adj, i, visited, stack)
    stack.append(v)

def get_transpose(adj):
    g = defaultdict(list)
    for v in adj :
        for i in adj[v]:
            g[i].append(v)
    return g

def print_sccs(adj) :
    V=len(adj)
    stack = []
    visited = [False] * V

    # Step 1: Fill vertices in stack according to their finishing times
    for i in range(V):
        if not visited[i]:
            fill_order(adj, i, visited, stack)

    # Step 2: Create a reversed graph
    gr = get_transpose(adj)

    # Step 3: Mark all vertices as not visited (for second DFS)
    visited = [False] * V

    # Step 4: Process all vertices in order defined by Stack
    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs_util(adj, v, visited)
            print()

adj=defaultdict(list) 
adj[0]=[2]
adj[1]=[0]
adj[2]=[1,3]
adj[3]=[4]
adj[4]=[3]
print("Kosaraju's Algorithm : ")
print_sccs(adj)
print("\n") 


## Bellman Ford shortest path algorithm 
def printArr(adj, dist):
	print("Vertex Distance from Source")
	for i in range(V):
		print("{0}\t\t{1}".format(i, dist[i]))

def BellmanFord(adj, src):
    V=len(adj)
    dist = [float("Inf")] * V
    dist[src] = 0
    for _ in range(V-1):
        for u in adj :
    	    for v, w in adj[u] : 
    		    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
    			    dist[v] = dist[u] + w
    for u in adj : 
        for v, w in adj[u] :
    	    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
    		    print("Graph contains negative weight cycle")
    		    return
    printArr(adj, dist)

adj=defaultdict(list) 
adj[0]=[(1,-1), (2,4)]
adj[1]=[(2,3), (3,2), (4,2)] 
adj[2]=[]
adj[3]=[(1,1), (2,5)] 
adj[4]=[(3,-3)]
print("Bellman Ford Algo")
BellmanFord(adj, 0)
print("\n") 



## Articulation Point 
# Python program to find articulation points in an undirected graph

from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.V = vertices 
		self.graph = defaultdict(list) 
		self.Time = 0
	
	def addEdge(self, u, v):        # function to add an edge to graph
		self.graph[u].append(v)
		self.graph[v].append(u)

	def APUtil(self, u, visited, ap, parent, low, disc):     # Count of children in current node		
		children = 0
		visited[u]= True    # Mark the current node as visited and print it
		disc[u] = self.Time    # Initialize discovery time 
		low[u] = self.Time     # Initialize low value
		self.Time += 1

		for v in self.graph[u]:     # Recur for all the vertices adjacent to this vertex
			# If v is not visited yet, then make it a child of u
			# in DFS tree and recur for it
			if visited[v] == False :
				parent[v] = u
				children += 1
				self.APUtil(v, visited, ap, parent, low, disc)

				# Check if the subtree rooted with v has a connection to
				# one of the ancestors of u
				low[u] = min(low[u], low[v])

				# u is an articulation point in following cases
				# (1) u is root of DFS tree and has two or more children.
				if parent[u] == -1 and children > 1:
					ap[u] = True

				#(2) If u is not root and low value of one of its child is more
				# than discovery value of u.
				if parent[u] != -1 and low[v] >= disc[u]:
					ap[u] = True
					
				# Update low value of u for parent function calls
			elif v != parent[u]:
				low[u] = min(low[u], disc[v])


	# The function to do DFS traversal. It uses recursive APUtil()
	def AP(self):

		# Mark all the vertices as not visited
		# and Initialize parent and visited,
		# and ap(articulation point) arrays
		visited = [False] * (self.V)
		disc = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)
		ap = [False] * (self.V) # To store articulation points

		# Call the recursive helper function
		# to find articulation points
		# in DFS tree rooted with vertex 'i'
		for i in range(self.V):
			if visited[i] == False:
				self.APUtil(i, visited, ap, parent, low, disc)

		for index, value in enumerate (ap):
			if value == True: print (index,end=" ")

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print ("\nArticulation points in first graph ")
g1.AP()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nArticulation points in second graph ")
g2.AP()

print("\n") 


# Simpler implementation 
from collections import defaultdict 
def APUtil(u, graph, visited, ap, parent, low, disc, Time) : 
    children=0 
    visited[u]=True 
    disc[u]=Time[0] 
    low[u]=Time[0]
    Time[0]+=1 

    for v in graph[u] : 
        if not visited[v] : 
            parent[v]=u 
            children+=1 
            APUtil(v, graph, visited, ap, parent, low, disc, Time) 
            low[u]=min(low[u], low[v])
            if parent[u]==-1 and children>1 : 
                ap[u]=True 
            if parent[u]!=-1 and low[v]>=disc[u] : 
                ap[u]=True 
        elif v!=parent[u] : 
            low[u]=min(low[u], disc[v]) 

def AP(vertices, edges) : 
    graph=defaultdict(list) 
    for u, v in edges : 
        graph[u].append(v) 
        graph[v].append(u) 
    visited=[False]*vertices
    disc=[float("inf")]*vertices
    low=[float("inf")]*vertices 
    parent=[-1]*vertices 
    ap=[False]*vertices
    Time=[0] 

    for i in range(vertices) : 
        if not visited[i] : 
            APUtil(i, graph, visited, ap, parent, low, disc, Time)  
    for index, value in enumerate(ap) :  
        if value : 
            print(index, end=" ")
print("\nArticulation points in first graph")
AP(5, [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)])

print("\nArticulation points in second graph")
AP(4, [(0, 1), (1, 2), (2, 3)])           
print("\n")



## Bridges in Graph 
def bridgeUtil(adj, u, visited, parent, low, disc, Time) : 
    visited[u]=True 
    disc[u]=Time[0] 
    low[u]=Time[0] 
    Time[0]+=1 
    for v in adj[u] : 
        if visited[v]==False : 
            parent[v]=u 
            bridgeUtil(adj, v, visited, parent, low, disc, Time) 
            low[u]=min(low[u], low[v]) 
            if low[v]>disc[u] : 
                print("%d %d" %(u,v)) 
        elif v!=parent[u] : 
            low[u]=min(low[u], disc[v]) 

def bridge(adj) :  
    V=len(adj) 
    visited=[False]*V 
    disc=[float("inf")]*V 
    low=[float("inf")]*V  
    parent=[-1]*V 
    Time=[0]
    for i in range(V) : 
        if visited[i]==False : 
            bridgeUtil(adj, i, visited, parent, low, disc, Time) 
adj=defaultdict(list)
adj[0]=[2,3]
adj[1]=[0]
adj[2]=[1]
adj[3]=[4] 
adj[4]=[] 

print("Bridges in first graph : ") 
bridge(adj) 

adj=defaultdict(list) 
adj[0]=[1]
adj[1]=[2]
adj[2]=[3]
adj[3]=[]
print("Bridges in second graph : ") 
bridge(adj) 
print("\n") 

