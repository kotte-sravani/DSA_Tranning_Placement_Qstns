# LeetCode Problem:680-Valid Palindrome II
# def ValidPal(s):
#     l=0
#     r=len(s)-1
#     while l<r:
#         if s[l]!=s[r]:
#             s_l=s[l+1:r+1]
#             s_r=s[l:r]
#             if (s_l == s_l[::-1]) or (s_r == s_r[::-1]):
#                 return True
#             else:
#                 return False
#         l+=1
#         r-=1
#     return True
# s="aba"
# print(ValidPal(s))

#Check if the list is Sorted and Duplicate is there or Not
# l=[1,2,3,4,5,7]
# flag=0
# for i in range(len(l)-1):
#     if l[i]>=l[i+1]:
#         flag=1
#         break
# if flag==1:
#     print("Nope")
# else:
#     print("Yes")

#Fixed Sliding Window
# l=[4,3,4,5,1,3,2,1,5,2,3,5]
# k=4
# sum=0
# for i in range(k):
#     sum+=l[i]
# m=sum
# for i in range(len(l)-k):
#     sum=sum+l[i+k]-l[i]
#     m=max(m,sum)
# print(m)

#Dynamic Sliding Window
# a=[2,5,1,7,10]
# k=14
# l,r,sum,m=0,0,0,0
# while r<len(a):
#     sum+=a[r]
#     if sum>=k:
#         sum-=a[l]
#         l+=1
#     if sum<k:
#         m=max(m,(r-l)+1)
#     r+=1
# print(m)

#Maximum Points you can Obtain from cards
# def maxScore(cardPoints):
#         n=len(cardPoints)
#         l_s=sum(cardPoints[:k])
#         r_s=0
#         m=l_s
#         for i in range(k):
#             l_s-=cardPoints[k-i-1]
#             r_s+=cardPoints[n-i-1]
#             m=max(m,l_s+r_s)
#         return m
# cardPoints=[1,2,3,4,5,6,1]
# k=3
# print(maxScore(cardPoints))

#LeetCode Problem: 45-Jump Game II
# def jump(nums):
#     l,r,jump=0,0,0
#     while r<len(nums)-1:
#         m=0
#         for i in range(l,r+1):
#             if i+nums[i]>m:
#                 m=i+nums[i]
#         l=r+1
#         r=m
#         jump=jump+1
#     return jump   
# nums=[2,3,1,1,4]
# print(jump(nums))
    
    
    

               
