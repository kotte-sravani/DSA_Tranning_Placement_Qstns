#LeetCode: Find The Town Judge
# def findJudge(n,trust):
#         if n==1:
#             return 1
#         d=collections.defaultdict(list)
#         for i,j in trust:
#             d[i].append(j)
#             d[j]
#         for i in d:
#             if len(d[i])==0:
#                 j=i
#                 break
#         else:
#             return -1
#         for i in d:
#             if j not in d[i] and i!=j:
#                  return -1
#         return j
    
#LeetCode: Number of Provinces
# def findCircleNum(isConnected):
#         if not isConnected:
#             return 0
#         n=len(isConnected)
#         visited=[0]*n
#         def dfs(node):
#             for ne in range(n):
#                 if isConnected[node][ne]==1 and not visited[ne]:
#                     visited[ne]=1
#                     dfs(ne)
#         count=0
#         for i in range(n):
#             if not visited[i]:
#                 visited[i]=1
#                 count+=1
#                 dfs(i)
#         return count

#Count all the no of paths in a Graph
# from collections import defaultdict
# edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
# graph=defaultdict(list)
# for u,v in edges:
#     graph[u].append(v)
# def count_path(start,end,path=[],c=0):
#     if path is None:
#         path=[]
#     path.append(start)
#     if start==end:
#         print(path)
#         c+=1
#     else:
#         for n in graph[start]:
#             if n not in path:
#                 c=count_path(n,end,path,c)
#     path.pop()
#     return c       
# start,end=0,5
# print(count_path(start,end))

#Print whether a cycle present in the Graph or not
# def cycle(graph):
#     visited=[False] * len(graph)
#     for n in range(len(graph)):
#         if not visited[n]:
#             q=[(n,-1)]
#             while q:
#                 node,prev=q.pop(0)
#                 visited[node]=True
#                 for ne in graph[node]:
#                     if not visited[ne]:
#                         q.append((ne,node))
#                     elif ne!=prev:
#                         return True
#     return False
#             
#             
# list=[[1],[0,2,3],[1,3],[1,2]]
# print(cycle(list))
