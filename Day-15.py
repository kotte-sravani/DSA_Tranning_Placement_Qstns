#Next Greater Element I: 
# def nextGreaterElement(nums1,nums2):
#     dict={n:i for i,n in enumerate(nums1)}
#     res=[-1]*len(nums1)
#     st=[]
#     for i in range(len(nums2)):
#         curr=nums2[i]
#         while st and curr>st[-1]:
#             val=st.pop()
#             index=dict[val]
#             res[index]=curr
#         if curr in dict:
#             st.append(curr)
#     return res
# nums1=[4,1,2]
# nums2=[1,3,4,2]
# print(nextGreaterElement(nums1,nums2))

#Online Stock Span:901-LeetCode Problem
# l=[1,2,3,4]
# st=[]
# for i in l:
#     st.append(i)
# st.pop()
# print(st[-1])
# print(st)

#Trees
# class Node:
#     def __init__(self,key):
#         self.left=None
#         self.right=None
#         self.val=key
# 
# def insert(root,key):
#     if root is None:
#         return Node(key)
#     else:
#         if key<root.val:
#             root.left=insert(root.left,key)
#         else:
#             root.right=insert(root.right,key)
#     return root
# 
# def inorder(root):
#     if root is None:
#         return
#     inorder(root.left)
#     print(root.val,end=" ")
#     inorder(root.right)
# 
# r=Node(7)
# r=insert(r,key=3)
# r=insert(r,key=5)
# r=insert(r,key=6)
# r=insert(r,key=8)
# inorder(r)


#HackerRank Problems
# class Node:
#     def _init_(self,key):
#         self.left=None
#         self.right=None
#         self.val=key
# def insert(root,key):
#     if root is None:
#         return Node(key)
#     else:
#         if key<root.val:
#             root.left=insert(root.left,key)
#         else:
#             root.right=insert(root.right,key)
#     return root
# def inorder(root):
#     if root is None:
#         return
#     inorder(root.left)
#     print(root.val,end=" ")
#     inorder(root.right)
# def preOrder(root):
#     if root is None:
#         return
#     print(root.val,end=" ")
#     preOrder(root.left)
#     preOrder(root.right)
# def postOrder(root):
#     if root is None:
#         return
#     postOrder(root.left)
#     postOrder(root.right)
#     print(root.val,end=" ")
# def levelOrder(root):
#     q=[]
#     q.append(root)
#     while len(q)!=0:
#         rt=q.pop(0)
#         print(rt.val,end=" ")
#         if rt.left is not None:
#             q.append(rt.left)
#         if rt.right is not None:
#             q.append(rt.right)
# c=Node(7)
# c=insert(c,key=3)
# c=insert(c,key=5)
# c=insert(c,key=2)
# c=insert(c,key=6)
# inorder(c)
# preOrder(c)
# postOrder(c)
# levelOrder(c)

#HackerRank Problem Is this binary tree
# def check_binary_search_tree_(root):
#     res=[]
#     def inOrder(root):
#         if root is None:
#             return
#         inOrder(root.left)
#         res.append(root.data)
#         inOrder(root.right)
#     inOrder(root)
#     for i in range(len(res)-1):
#         if res[i]>=res[i+1]:
#             return False
#     return True

#Height of a Binary tree
# def height(root):
#     if root is None:
#         return -1
#     return 1+max(height(root.left),height(root.right))

#Tree: Top View Hackerrank problem
# def topView(root):
#     q=[]
#     d=dict()
#     root.level=0
#     q.append(root)
#     while len(q)!=0:
#         root=q.pop(0)
#         if root.level not in d:
#             d[root.level]=root.info
#         if root.left is not None:
#             q.append(root.left)
#             root.left.level=root.level-1
#         if root.right is not None:
#             q.append(root.right)
#             root.right.level=root.level+1
#     for key in sorted(d.key()):
#         print(d[key],end=" ")

#Combination of two values upto n
# n=10
# q=[]
# q.append("5")
# q.append("6")
# count=0
# while count<n:
#     t=q.pop(0)
#     print(t,end=" ")
#     q.append(t+"5")
#     q.append(t+"6")
#     count+=1