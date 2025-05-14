######################################### BASIC RECURSSION #######################################
# RECURSSION PRINT NUMS # N=5 1234554321 PATTERN 
# def fun(n, i=1):
#     if i > n:
#         return
#     print(i, end=" ")
#     fun(n, i + 1)
#     print(i, end=" ")
# n=int(input())
# fun(n)  

#PRINTING 54321 PATTERN Tail Recurssion 
# def fun(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun(n-1)
# n=5
# fun(n)

#PRINTING 12345 PATTERN Head Recurssion
# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end=" ")
# n=5
# fun(n)

# PRINTING 12345 AND SHOULD PRINT 200 ALSO 
# def fun(n):
#     if n==0:
#         return 200
#     x = fun(n-1)
#     print(n,end=" ")
#     return x
# n=5
# print(fun(n))

#PRINTING NUMBERS 5432112345 PATTEREN
# def fun(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun(n-1)
#     print(n,end=" ")
# n=5
# fun(n)

# PRINTING 5432112345 REMOVE 1 IN IT AND PRINT 543212345
# def fun(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun(n-1)
#     if n!=1:
#         print(n,end=" ")
# n=5
# fun(n)

# PRINTING ODD AND EVEN NUMBERS IN 543212345
# def fun(n):
#     if n==0:
#         return
#     if n%2!=0:
#         print(n,end=" ")
#     fun(n-1)
#     if n!=1:
#         if n%2!=0:
#             print(n,end=" ")
# n=int(input())
# fun(n)

# PRINTING THE PATTERN 1234554321 METHOD 2
# def fun(n, m=0):
#     if n==m:
#         return
#     print(m+1, end=" ")
#     fun(n,m+1)
#     print(m+1, end=" ")
#     
# n=int(input())
# fun(n)

#FACTORIAL OF GIVEN NUMBERS
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# x=int(input())
# print(fact(x))

#FINDING THE GIVEN NUM IS PRIME OR NOT
# def is_prime(n, i=2):
#     if n <= 2:
#         return n == 2  
#     if n % i == 0:
#         return False
#     if i * i > n:
#         return True
#     return is_prime(n, i + 1)
# n=int(input())
# if is_prime(n):
#     print("Prime")
# else:
#     print("Not Prime")

#FIBONACCI SERIES USING RECURSSION
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
x=int(input())
print(fib(x))

#REVERSE THE GIVE NUMBER
# def rev_num(n, rev=0):
#     if n == 0:
#         return rev
#     return rev_num(n // 10, rev * 10 + n % 10)
# n=int(input())
# print(rev_num(n))

############PRIME NUMBER OR NOT IN ANOTHER METHOD########################
# n=int(input())
# flag=0
# for i in range(2,n//2):  #(or use)for i in range(2,int(n**(1/2))+1): # optimizied code
#     if n%i==0:
#         flag+=1
#         break
# if flag==0:
#     print("Prime")
# else:
#     print("Not Prime")

#############REVERSE THE NUMBER ANOTHER METHOD#########################
# def rev(n,re=0):
#     if n==0:
#         return re
#     d=n%10
#     re=(re*10)+d
#     return rev(n//10,re)
# 
# num=int(input())
# print(rev(num))


# N=15 reduce the num to 1 if it is odd num add 1 or reduce 1 if it is even divide by 2 find the minimum steps to reach 1   
# def fun(n):
#     if n==1:
#         return 0
#     elif n%2==0:
#         return 1 + fun(n//2)
#     else:
#         return 1+min(fun(n-1),fun(n+1))
# n = 15
# print(fun(n))

#SUM OF ALL ELEMENTS IN THE LIST USING RECRUSSION
# def fun(list,i=0):
#     if i==len(list):
#         return 0
#     return list[i] + fun(list,i+1)
# 
# list= [1, 2, 3, 4, 5]
# print(fun(list))

#COUNT THE PRIME NUMBERS IN THE LIST USING RECRUSSION
# def prime(n, i=2):
#     if i * i > n:
#         return True
#     if n%i == 0:
#         return False
#     return prime(n,i+1)
# 
# def fun(l,i=0):
#     if i==len(l):
#         return 0
#     if prime(l[i]):
#         return 1+fun(l,i+1)
#     else:
#         return fun(l,i+1)
# 
# l=[4, 5, 6, 3, 11]
# print(fun(l))
        
