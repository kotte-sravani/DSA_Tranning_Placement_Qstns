#LeetCode Problem:860 Lemonade Change
# def lemonadeChange(bills):
#     f=0
#     t=0
#     for i in bills:
#         if i==5:
#             f+=1
#         elif i==10:
#             if f>0:
#                 t+=1
#                 f-=1
#             else:
#                 return False
#         else:
#             if t>0 and f>0:
#                 t-=1
#                 f-=1
#             elif f>=3:
#                 f-=3
#             else:
#                 return False
#     return True
# bills = [5,5,5,10,20]
# print(lemonadeChange(bills))

#LeetCode Problem:55 Jump Game
# def canJump(nums):
#     petrol=0
#     for p in nums:
#         if petrol<0:
#             return False
#         elif p>petrol:
#             petrol=p
#         petrol-=1
#     return True
# nums=[2,3,1,1,4]
# print(canJump(nums))

#Geeks for geeks:Shortest Job first
# def solve(bt):
#     bt.sort()
#     n=len(bt)
#     wt=[0]*n
#     for i in range(1,n):
#         wt[i]=wt[i-1]+bt[i-1]
#     return int(sum(wt)/n)
# n=5
# bt=[4,3,7,1,2]
# print(solve(bt))

#LeetCode problem:455 Assign Cookies
# def findContentChildren(g):
#     g.sort()
#     s.sort()
#     i,j=0,0
#     c=0
#     while i<len(g) and j<len(s):
#         if s[j]>=g[i]:
#             c+=1
#             i+=1
#         j+=1
#     return c
# g=[1,2,3]
# s=[1,1]
# print(findContentChildren(g))

#Geeks for geeks: N Meeting in one room
# def maximumMeetings(start,end):
#     m=sorted(zip(start,end),key=lambda x:(x[1],x[0]))
#     c=0
#     l=-1
#     for s,e in m:
#         if s>l:
#             c+=1
#             l=e
#     return c
# start=[1,3,0,5,8,5]
# end=[2,4,6,7,9,9]
# print(maximumMeetings(start,end))

#Interview based Problem
# s=input()
# res=[]
# count=1
# for i in range(len(s)):
#     if i>0 and s[i]==s[i-1]:
#         count+=1
#     else:
#         count=1
#     if count<=2:
#         res.append(s[i])
# print("".join(res))   # use join to get the output in string format

#print reduce the string to the minimum length 
# s="abba"
# res=[]
# for i in s:
#     if res and res[-1]==i:
#         res.pop()
#     else:
#         res.append(1)
# print("".join(s))

#Length of the longest palindrome subset

#String Compression: Input: "aaaabbbc" Output: "a4b3c1"
# s="aaaabbbc"
# res=[]
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#     else:
#         res.append(s[i-1]+str(c))
#         c=1
# res.append(s[-1]+str(c))
# print("".join(res))

#LeetCode Problem:345 Reverse vowels of a string
# def reverseVowels(s):
#     v=set("aeiouAEIOU")
#     s=list(s)
#     l=0
#     r=len(s)-1
#     while l<r:
#         if s[l] not in v:
#             l+=1
#         elif s[r] not in v:
#             r-=1
#         else:
#             s[l],s[r]=s[r],s[l]
#             l+=1
#             r-=1
#     return "".join(s)
# s="IceCreAm"
# print(reverseVowels(s))
