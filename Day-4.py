#SUM OF N NATURAL NUMBERS USING RECRUSIONS
#PARAMETERIZED RECRUSION
# def fun(n,sum):
#     if n<1:
#         print(sum)
#         return
#     fun(n-1,sum+n)
#     
# n=5
# fun(n,sum=0)

#SUBSET OF A LIST
# def sub(arr,i=0,res=[]):
#     if i==len(arr):
#         print(res)
#         return
#     sub(arr,i+1,res+[arr[i]])  #take
#     sub(arr,i+1,res)      #not take
#     
# l=[1,2,3]
# sub(l)

#PRINTING SUBSETS WITH THE SUM 
# def sub(arr,k,i=0,res=[]):
#     if i==len(arr):
#         return
#     if sum(res)==k:
#         return True
#     else:
#         return False
#     sub(arr,k,i+1,res+[arr[i]])  #take
#     sub(arr,k,i+1,res)      #not take
#     
# l=[1,2,3,6]
# k=7
# print(sub(l,k))

#SUBSET SUM OPTIMIZED CODE
# def fun(arr,i,k):
#     if k==0:
#         return True
#     if i==0:
#         return False
#     if arr[i-1]>k:
#         return fun(arr,i-1,k)
#     return fun(arr,i-1,k) or fun(arr,i-1,k-arr[i-1])
# 
# l=[1,2,3,8]
# k=5
# print(fun(l,len(l),k))

#PRINT THE SUBSETS HAVING THE SUM
# def sub(arr,k,i=0,res=[]):
#     if i==len(arr):
#         if sum(res)==k:
#             print(res)
#         return
#     sub(arr,k,i+1,res+[arr[i]])      #take
#     sub(arr,k,i+1,res)           #not take
#     
# l=[1,2,3,4,8]
# k=5
# sub(l,k)

#FREQUENCY OF THE ELEMENT IN THE LIST
# def fun(arr,k,i=0):
#     if i==len(arr):
#         return 0
#     if arr[i]==k:
#         return 1+fun(arr,k,i+1)
#     else:
#         return fun(arr,k,i+1)
# l=[1,2,3,4,5,1]
# k=1
# print(fun(l,k))

#
# def frq(l,t,i=0):
#     if i==len(l):
#         return 0
#     if l[i]==t:
#         return 1+frq(l,t,i+1)
#     return frq(l,t,i+1)
# 
# l=[1,1,3,2,2,3,3,3]
# target=3
# print(frq(l,target))

#CODEFORCE PROBLEM 1560A DISLIKE OF THREES
# t=int(input())
# for _ in range(t):
#     i=1
#     count=0
#     k=int(input())
#     while(1):
#         if i%3!=0 and i%10!=3:
#             count+=1
#             if count==k:
#                 print(i)
#                 break
#         i+=1