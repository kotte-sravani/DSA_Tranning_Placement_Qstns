#Search key element in BST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def search(root,key):
#     if root is None:
#         return False
#     if root.data == key:
#         return True
#     elif root.data>key:
#         return search(root.left,key)
#     else:
#         return search(root.right,key)
#     
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(search(root,key=1))

#Search root elements in Binary Tree
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def search_bi(root,key):
#     if root is None:
#         return False
#     if root.data == key:
#         return True
#     return search_bi(root.left,key) or search_bi(root.right,key)
# 
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(search_bi(root,key=1))

#Print all the paths from the root to the leaf nodes
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def path(root,p=[]):
#     if root is None:
#         return
#     p.append(str(root.data))
#     if root.left is None and root.right is None:
#         print(" ".join(p))
#     path(root.left,p)
#     path(root.right,p)
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# path(root)

#Print the Max sum of the path
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def path_sum(root,p=[],s=0):
#     if root is None:
#         return 0
#     p.append(str(root.data))
#     s+=root.data
#     if root.left is None and root.right is None:
#         return s
#     l_s=path_sum(root.left,p,s)
#     r_s=path_sum(root.right,p,s)
#     return max(s,l_s,r_s)
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(path_sum(root))

#DFS Traversal of a Graph
# def dfs(graph,n,visited=set()):
#     if n not in visited:
#         print(n,end=" ")
#         visited.add(n)
#         for i in graph[n]:
#             dfs(graph,i,visited)
#             
# graph = {
#     'A':['B','C'],
#     'B':['A','D','E'],
#     'C':['A','F'],
#     'D':['B'],
#     'E':['B','F'],
#     'F':['C','E']}
# dfs(graph,n='A')

#BFS Traversal of a Graph
# def bfs(graph,start):
#     visited=set()
#     q=[start]
#     while q:
#         n=q.pop(0)
#         if n not in visited:
#             print(n,end=" ")
#             visited.add(n)
#             q.extend(graph[n])
#             
# graph = {
#     'A':['B','C'],
#     'B':['A','D','E'],
#     'C':['A','F'],
#     'D':['B'],
#     'E':['B','F'],
#     'F':['C','E']}
# print()
# bfs(graph,start='A')

#
# from collections import defaultdict
# edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
# graph=defaultdict(list)
# for u,v in edges:
#     graph[u].append(v)       
#     graph[v].append(u)     #remove the line if it is not directed graph
#     
# def path(graph,start,end):
#     visited=set()
#     def dfs(val):
#         if val==end:
#             return True
#         visited.add(val)
#         for n  in graph[val]:
#             if n not in visited:
#                 if dfs(n):
#                     return True
#         return False
#     return dfs(start)
#     
# start,end=0,5
# print(path(graph,start,end))

#Directed graph: BFS Traversal
# from collections import defaultdict
# edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
# graph=defaultdict(list)
# for u,v in edges:
#     graph[u].append(v)
#     graph[v].append(u)
# def path(graph,start,end):
#     v=set()
#     q=[]
#     q.append(start)
#     v.add(start)
#     while q:
#         node=q.pop(0)
#         if node==end:
#             return True
#         for i in graph[node]:
#             if i not in v:
#                 v.add(i)
#                 q.append(i)
#     return False
# start,end=0,5
# print(path(graph,start,end))


#Directed graph: Print all the paths
# from collections import defaultdict
# edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
# graph=defaultdict(list)
# for u,v in edges:
#     graph[u].append(v)
# def print_path(start,end,path=[]):
#     path.append(start)
#     if start==end:
#         print(path)
#     else:
#         for n in graph[start]:
#             if n not in path:
#                 print_path(n,end,path)
#     path.pop()
#                 
# start,end=0,5
# print_path(start,end)

#LeetCode: Find Center of Star Graph
# def findCenter(edges):
#         if(edges[0][0] in edges[1]):
#             return edges[0][0]
#         else:
#             return edges[0][1]

