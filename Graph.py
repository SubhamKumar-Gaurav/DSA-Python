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