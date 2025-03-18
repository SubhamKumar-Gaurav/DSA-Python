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


