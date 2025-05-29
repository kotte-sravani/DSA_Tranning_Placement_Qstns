#BST LeetCode:Lowest Common Ancestor
# class Node:
#     def _init_(self, info): 
#         self.info = info  
#         self.left = None  
#         self.right = None 
#         self.level = None 
# def lca(root, v1, v2):
#   if v1<root.info and v2<root.info:
#     return lca(root.left,v1,v2)
#   elif v1>root.info and v2>root.info:
#     return lca(root.right,v1,v2)
#   else:
#     return  root


############## BASIC TREE PROBLEMS ##############
#Sum of all the Nodes in the BST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def sum_all(root):
#         if root is None:
#             return 0
#         return root.data + Node.sum_all(root.left) + Node.sum_all(root.right)
#         
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(Node.sum_all(root))

#Sum of even nodes in BST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def even_sum(root):
#         if root is None:
#             return 0
#         even_sum=0
#         if root.data % 2 == 0:
#             even_sum=root.data
#         return even_sum + Node.even_sum(root.left) + Node.even_sum(root.right)
# 
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(Node.even_sum(root))

#Sum of odd nodes in BST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def odd_sum(self):
#         t=0
#         if self.data%2!=0:
#             t=self.data
#         if self.left is not None:
#             t+=self.left.odd_sum()
#         if self.right is not None:
#             t+=self.right.odd_sum()
#         return t
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(root.odd_sum())

#Print the Leaf nodes in BST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def print_leaf(self):
#         if self.left is None and self.right is None:
#             print(self.data,end=" ")
#         if self.left:
#             self.left.print_leaf()
#         if self.right:
#             self.right.print_leaf()
# 
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(root.print_leaf())

#Print prime nodes in BST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def is_prime(self,num):
#         if num<2:
#             return False
#         for i in range(2,int(num**0.5)+1):
#             if num % i==0:
#                 return False
#         return True
#     def print_prime(self):
#         if self.is_prime(self.data):
#             print(self.data,end=" ")
#         if self.left:
#             self.left.print_prime()
#         if self.right:
#             self.right.print_prime()
# 
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(root.print_prime())

#Find the K-th largest Element
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#     def klargest(self,k):
#         def inorder(node,l):
#             if node is None:
#                 return
#             inorder(node.right,l)
#             l.append(node.data)
#             inorder(node.left,l)
#         l=[]
#         inorder(self,l)
#         return l[k-1]
# 
# root = Node(5)
# root.left = Node(2)
# root.right = Node(7)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(8)
# print(root.klargest(3))

#Find the K-th Smallest Element
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#     def ksmallest(self,k):
#         def inorder(node,l):
#             if node is None:
#                 return
#             inorder(node.left,l)
#             l.append(node.data)
#             inorder(node.right,l)
#         l=[]
#         inorder(self,l)
#         return l[k-1]
# 
# root = Node(5)
# root.left = Node(2)
# root.right = Node(7)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(8)
# print(root.ksmallest(3))

#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#(LeetCode Problem:100 - Same Tree)
# def isSameTree(self,p,q):
#         if not p and not q:
#             return True
#         if not p or not q or p.val != q.val:
#             return False
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#Find the count of leaf nodes in BST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def count_leaf(self):
#         if self.left is None and self.right is None:
#             return 1
#         c=0
#         if self.left:
#             c+=self.left.count_leaf()
#         if self.right:
#             c+=self.right.count_leaf()
#         return c
# 
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print(root.count_leaf())

#Invert Binary Tree (LeetCode:100)
# def invertTree(self,root):
#         if not root:
#             return None
#         root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
#         return root

#Top View in Binary Tree
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def topView(root):
#     if not root:
#         return
#     q=[]
#     d=dict()
#     q.append((root,0))
#     while q:
#         node,e=q.pop(0)
#         if e not in d:
#             d[e]=node.data
#         if node.left:
#             q.append((node.left,e-1))
#         if node.right:
#             q.append((node.right,e+1))
#     for key in sorted(d):
#         print(d[key],end=" ")
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# topView(root)

#Buttom View in Binary Tree
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def ButtomView(root):
#     q=[]
#     d=dict()
#     q.append((root,0))
#     while q:
#         node,val=q.pop(0)
#         d[val]=node.data
#         if node.left:
#             q.append((node.left,val-1))
#         if node.right:
#             q.append((node.right,val+1))
#     for key in sorted(d):
#         print(d[key],end=" ")
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print()
# ButtomView(root)

#Left View in Binary Tree
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def leftView(root):
#     if not root:
#         return
#     q=[]
#     d=dict()
#     q.append((root,0))
#     while q:
#         node,e=q.pop(0)
#         if e not in d:
#             d[e]=node.data
#         if node.left:
#             q.append((node.left,e+1))
#         if node.right:
#             q.append((node.right,e+1))
#     for key in sorted(d):
#         print(d[key],end=" ")
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print()
# leftView(root)

#Right View in Binary Tree
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def rightView(root):
#     if not root:
#         return
#     q=[]
#     d=dict()
#     q.append((root,0))
#     while q:
#         node,e=q.pop(0)
#         d[e]=node.data
#         if node.left:
#             q.append((node.left,e+1))
#         if node.right:
#             q.append((node.right,e+1))
#     for key in sorted(d):
#         print(d[key],end=" ")
# root=Node(5)
# root.left=Node(2)
# root.right=Node(7)
# root.left.left=Node(1)
# root.left.right=Node(3)
# root.right.left=Node(6)
# root.right.right=Node(8)
# print()
# rightView(root)

#Huffman Decoding: HackerRank
# def decodeHuff(root, s):
#     temp=root
#     res=[]
#     for i in s:
#         if i=="0":
#             temp=temp.left
#         else:
#             temp=temp.right
#         if temp.left is None and temp.right is None:
#             res.append(temp.data)
#             temp=root
#     print("".join(res))