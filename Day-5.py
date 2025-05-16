# #FINDING THE SUM OF 2D MATRIX BY TRACING
# m=[[1,2,3],[4,5,6],[7,8,9]]
# rows=len(m)
# cols=len(m[0])
# sum=0
# for i in range(rows):
#     for j in range(cols):
#         sum+=m[i][j]
# print(sum)

#FINDING THE PRIME NUMBERS IN THE 2D MATRIX
# def fun(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) +1):
#         if n%i==0:
#             return False
#         return True
# def prime(matrix):
#     return [num for row in matrix for num in row if fun(num)]
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(prime(matrix))

#PATH TO REACH THE EXIT
# def path(m,i,j,p,n):
#     if i==n-1 and j==n-1:
#         print(p)
#         return
#     if i+1<n and m[i+1][j]==1:
#         path(m,i+1,j,p+"D",n)
#     if j+1<n and m[i][j+1]==1:
#         path(m,i,j+1,p+"R",n)   
# m=[[1,1,1,0],
#    [0,1,1,0],
#    [0,1,1,1],
#    [0,0,0,1]]
# path(m,0,0,"",len(m))

#FOREST FIRE(1'S ARE TREES AND 0'S ARE THE LAND AND TREES COUGHT FIRE SO FIND THE TREES WHICH ARE NOT FIRED)
# def fire(m,i,j):
#     c=0
#     if not m:
#         return
#     if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
#         return
#     m[i][j]=2
#     fire(m,i+1,j)
#     fire(m,i-1,j)
#     fire(m,i,j+1)
#     fire(m,i,j-1)
#     for i in range(len(m)):
#         for j in range(len(m[0])):
#             if m[i][j]==1:
#                 c+=1
#     return c
#     
# m=[[1,1,1,0,1],
#    [0,1,1,1,0],
#    [0,0,0,1,0],
#    [1,1,0,0,1]]
# print(fire(m,0,1))

#LEETCODE PROBLEM NUMBER OF ISLANDS
# def island(m,i,j):
#     if not m:
#         return 0
#     if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
#         return 0
#     m[i][j]=2
#     island(m,i+1,j)
#     island(m,i-1,j)
#     island(m,i,j+1)
#     island(m,i,j-1)
#     
# m=[[1,1,1,0,1],
#    [0,1,1,1,0],
#    [0,0,0,1,0],
#    [1,1,0,0,1]]
# c=0
# for i in range(len(m)):
#         for j in range(len(m[0])):
#             if m[i][j]==1:
#                 island(m,i,j)
#                 c+=1
# print(c)

#POSSIBLE BINARY NUMBERS
# def bi(n,s=""):
#     if n==0:
#         print(s)
#         return
#     bi(n-1,s+"0")
#     bi(n-1,s+"1")
# n=int(input())
# bi(n)

#PRINTING COUNT OF VALID PARANTHESIS
# def par(n,s=0,e=0,p=""):
#     if s==n and e==n:
#         print(p)
#         return
#     if s<n:
#         par(n,s+1,e,p+"(")
#     if e<s:
#         par(n,s,e+1,p+")")
# n=int(input())
# par(n)

#LEETCODE PROBLEM OF BEST TIME TO BUY AND SELL STOCK
# def maxProfit(prices):
#     mp=prices[0]
#     m=0
#     for i in prices:
#         m=max(m,i-mp)
#         mp=min(mp,i)
#     return m
# p=[7,1,5,3,6,4]
# print(maxProfit(p))

#LEETCODE PROBLEM OF FACTORIAL TRAILING ZEROES ### IMP QSTN ###
# def fun(n):
#     if(n<5):
#         return 0
#     sum=0
#     while(n>=5):
#         sum=sum+n//5
#         n=n//5
#     return sum
# n=int(input())
# print(fun(n))