# Fibnoacci series using recrusion Time Complexity:O(2^n)
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)
# n=6
# print(fib(n))

#Memorization - Recrusion(Top-down approach)
#Optimized Code Fibnoacci series using Dynamic Programming 
# def fib(n):
#     if n<=1:                              #Time Complexity: O(2n)
#         return n
#     if memo[n]!=-1:
#         return memo[n]
#     memo[n]=fib(n-1)+fib(n-2)
#     return memo[n]
# 
# n=6
# memo=[-1]*(n+1)
# print(fib(n))

#Tabulation (Buttom-Up approach) using loops Time Complexity: O(n)
# n=6
# dp=[0]*(n+1)  #dp=[-1]*(n+1)
# dp[1]=1     #down line - dp[0]=0
# for i in range(2,n+1):
#     dp[i]=dp[i-1]+dp[i-2]   
# print(dp[n])

#Optimized code removing table Time Complexity: O(n),Space Complexity: O(1)
# n=6
# a,b=0,1
# for _ in range(2,n+1):
#     fib=a+b
#     a=b
#     b=fib
# print(fib)

#How to solve:
#Convert the problem in terms of index
#Do all the possible stuff on that index
#Count all ways: Find the sum

#Climbing Stairs
# def climbStairs(n):
#         if n<=2:
#             return n
#         dp=[0]*(n+1)
#         dp[1]=1
#         dp[2]=2
#         for i in range(3,n+1):
#             dp[i]=dp[i-1]+dp[i-2]
#         return dp[n] 
# n=3
# print(climbStairs(n))

#Frog Jump:403
# def frog(ind):
#     if ind == 0:
#          return 0
#     j1=frog(ind-1)+abs(rock[ind]-rock[ind-1])
#     if ind>1:
#         j2=frog(ind-2)+abs(rock[ind]-rock[ind-2])
#         return min(j1,j2)
#     else:
#         return j1
# rock=[30,10,60,10,60,50]
# print(frog(len(rock)-1))

#Frog Jump using Memorization 
# def frog(ind,memo):
#     if ind == 0:
#          return 0
#     if memo[ind]!=-1:
#         return memo[ind]
#     j1=frog(ind-1,memo)+abs(rock[ind]-rock[ind-1])
#     if ind>1:
#         j2=frog(ind-2,memo)+abs(rock[ind]-rock[ind-2])
#         memo[ind]=min(j1,j2)
#         return memo[ind]
#     else:
#         memo[ind]=j1
#     return memo[ind]
# 
# rock=[30,10,60,10,60,50]
# n=len(rock)
# memo=[-1]*(n+1)
# print(frog(n-1,memo))

#Frog Jump using Tabulation
# rock=[30,10,60,10,60,50]
# n=len(rock)
# memo=[0]*n
# for i in range(1,n):
#     j1=memo[i-1]+abs(rock[i]-rock[i-1])
#     j2=float('inf')
#     if i>1:
#         j2=memo[i-2]+abs(rock[i]-rock[i-2])
#         memo[i]=min(j1,j2)
# print(memo[n-1])
    
#Coin Change
# arr=[1,2,5,10]
# t=12
# n=len(arr)
# dp=[[False]*(t+1) for _ in range(n+1)]
# for i in range(n+1):
#     dp[i][0]=True
# for i in range(1,n+1):
#     for j in range(1,t+1):
#         if arr[i-1]>j:
#             dp[i][j]=dp[i-1][j]
#         else:
#             dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
#             
# if dp[n][t]:
#     print("Yes, can make an amount")
# else:
#     print("No, can't")

