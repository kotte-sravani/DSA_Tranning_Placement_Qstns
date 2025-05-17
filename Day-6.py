#Bubble Sort
# arr=[3,4,7,2,9,6,1,0]
# for i in range(len(arr)):
#     flag=False
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[i]:
#             arr[i],arr[j]=arr[j],arr[i]
#             flag=True
#     if not flag:
#         break
# print(arr)

#Insertion Sort
# arr=list(map(int,input().split()))
# min_ind=arr[0]
# for i in range(0,len(arr)):
#     min_ind=i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_ind]:
#             min_ind=j
#     arr[i],arr[min_ind]=arr[min_ind],arr[i]
# print(arr)

#Insertion Sort Optimized Code 
# arr=[33,18,45,7,92,77,88]
# for i in range(len(arr)):
#     min=i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min]:
#             min=j
#     arr[i],arr[min]=arr[min],arr[i]
# print(arr)

#Selection Sort
# arr=[10,40,30,20,50]
# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and key<arr[j]:
#         arr[j+1]=arr[j]
#         j-=1
#         arr[j+1]=key
# print(arr)

#Input=[3,6,1,7,4,2,5] Output=[6,4,2,1,3,5,7]
# l=[3,6,1,7,4,2,5]
# l.sort()
# res=[]
# for i in l:
#     if i%2!=0:
#         res.append(i)
#     else:
#         res.insert(0,i)
# print(res)

#Finding the Largest Number in list
# l=[3,2,6,4,7,1,5]    #Brutforce Approach
# l.sort()
# print(l[-1])
# 
# l=[7,2,3,6,1]        #Optimized code
# m=l[0]
# for i in l:
#     if i>m:
#         m=i
# print(m)

#Second Largest Element in the list
# l=[3,2,6,4,7,1,5]
# m1=0
# for i in l:
#     if i>m1:
#         m1=i
# m2=0
# for i in l:
#     if i>m2 and i!=m1:
#         m2=i
# print(m2)

#K-th Largest Number in a list
# l=[3,2,6,4,7,1,5]
# k=4
# n=len(l)
# for i in range(k):
#     for j in range(0,n-1-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l[-k])

#Input=[2,3,5,1,6,9,8] Output=[2,3,1,5,6,9,8]
# l=[2,3,5,1,6,9,8]
# k=2
# for i in range(k,len(l)):
#     for j in range(2,len(l)-2):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

#Input=[[1,2],[5,1],[2,4],[6,3]] Output=[[5,1],[1,2],[6,3],[2,4]]
# l=[[1,2],[5,1],[2,4],[6,3]]
# for i in range(len(l)):
#     for j in range(0,len(l)-1-i):
#         if l[j][1]>l[j+1][1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

#Input=[[20,12,11],[10,5,22],[16,7,30]] Output=[[10,5,22],[16,7,30],[20,12,11]]
# l=[[20,12,11],[10,5,22],[16,7,30]]
# for i in range(len(l)):
#     for j in range(0,len(l)-1-i):
#       if l[j][1]>l[j+1][1]:
#           l[j],l[j+1]=l[j+1],l[j]
# print(l)

#Printing the prime 
# def prime(x):
#     for i in x:
#         for j in range(2,int(i**0.5) + 1):
#             if i%j==0:
#                 break
#             return i
#     return None
# l=[[20,12,11],[10,5,22],[16,7,30]]
# b=[]
# n=len(l)
# for i in l:
#     b.append(prime(i))
# for i in range(n):
#     for j in range(0,n-i-1):
#         if b[j]>b[j+1]:
#             b[j],b[j+1]=b[j+1],b[j]
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

#Sorting the strings based on the length
# a=["aaa","aaaaaaa","aa","aaaaa"]
# res=sorted(a,key=len)
# print(res)

#Sorting based on Frequency
# a=['a','b','b','b','c','c']
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# sc=sorted(b.items(),key=lambda item:item[1])
# res=""
# for c,count in sc:
#     res+=c*count
# print(res)

#Sorting based on Frequency
# s="baabaaccc"
# frq={}
# for c in s:
#     if c in frq:
#         frq[c]+=1
#     else:
#         frq[c]=1
# sc=sorted(frq.items(),key=lambda item:item[1])
# res=""
# for c,count in sc:
#     res+=c*count
# print(res)

#Input=[[[1,0,0,1],[1,0,0,0],[0,0,1,0],[0,1,1,0]]
# m=[[1,0,0,1],
#    [1,0,0,0],
#    [0,0,1,0],
#    [0,1,1,0]]
# a=[5,10,3,4]
# for i in range(len(m)):
#     sum=0
#     for j in range(len(m[0])):
#         if m[i][j]==1:
#             sum+=a[j]
#     print(sum)
