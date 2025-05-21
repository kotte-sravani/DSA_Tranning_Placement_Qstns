#Binary Search LeetCode Problem:704 
# def Binary_search(nums):
#     l=0
#     r=len(nums)-1
#     while l<=r:
#         mid=(r+l)//2
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]>target:
#             r=mid-1
#         else:
#             l=mid+1
#     return -1
# nums = [-1,0,3,5,9,12]
# target = 0
# print(Binary_search(nums))

#Search a 2D Matrix
# def searchMatrix(matrix, target):
#     m=len(matrix)
#     n=len(matrix[0])
#     l=0
#     r=m*n-1
#     while l<=r:
#         mid=(l+r)//2
#         i=mid//m
#         j=mid%m
#         num=matrix[i][j]
#         if num==target:
#             return True
#         elif num<target:
#             l=mid+1
#         else:
#             r=mid-1
#     return False
# matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target=3
# print(searchMatrix(matrix,target))

#Aggressive Cows: Geeks for Geeks Problem
# def cankeep(stalls,k,d):
#     c=1
#     lp=stalls[0]
#     for i in range(1,len(stalls)):
#         if stalls[i]-lp>=d:
#             c+=1
#             lp=stalls[i]
#             if c==k:
#                 return True
#     return False
# def aggressiveCows(stalls, k):
#     l=1
#     r=stalls[-1]-stalls[0]
#     bd=0
#     while(l<=r):
#         mid=(l+r)//2
#         if cankeep(stalls,k,mid):
#             bd=mid
#             l=mid+1
#         else:
#             r=mid-1
#     return bd
# stalls=[1,2,4,8,9]
# k=3
# print(aggressiveCows(stalls,k))

#Nim Game in LeetCode                                                             
# def canWinNim(n):
#     return n%4!=0 
# n=1
# print(canWinNim(n))

#Candies and Two Sisters problem i CodeForces
# t=int(input())  
# for i in range(t):
#     n=int(input())
#     if n<3:
#         print("0")
#     else:
#         print((n-1)//2)
        
#CodeForces Problem Remove Smallest
# t=int(input())
# for i in range(t):  
#     n=int(input())  
#     arr=list(map(int,input().split()))  
#     arr.sort()  
#     for j in range(n-1):  
#         if abs(arr[j]-arr[j+1])>1:  
#             print("NO")  
#             break  
#     else:  
#         print("YES")  
