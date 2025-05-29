#Intersetion of two linked lists
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=Node
#     def getIntersectionNode(headA,headB):
#         i=headA
#         j=headB
#         while i!=j:
#             if i:
#                 i=i.next
#             else:
#                 i=headB
#             if j:
#                 j=j.next
#             else:
#                 j=headA   
#         return j
#     

    
#Reverse the linked list
# class Solution:
#     def reverseList(self, head):
#         prev=None
#         curr=head
#         while curr!=None:
#             next_node=curr.next  
#             curr.next=prev  
#             prev=curr  
#             curr=next_node  
#         return prev


#Palindrome Linked List: LeetCode 234
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         fast = head
#         slow = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         prev=None
#         curr=slow
#         while curr!=None:
#             temp=curr.next  
#             curr.next=prev  
#             prev=curr  
#             curr=temp  
#         l,r=head,prev  
#         while r!=None:
#             if l.val!=r.val:
#                 return False
#             l=l.next
#             r=r.next
#         return True


#Bubble Sort using linked list
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
# class Linked_list:
#     def _init_(self):
#         self.head=None
#     def append(self,val):
#         temp=self.head
#         while temp.next!=None:
#             temp=temp.next
#         temp.next=Node(val)
#     def bubble(self):
#         e=None  
#         while self.head.next!=e:
#             c=self.head
#             while c.next!=e:  
#                 if c.data>c.next.data:
#                     c.data,c.next.data=c.next.data,c.data  
#                 c=c.next
#             e=c  
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
# l1=Linked_list()
# l1.head=Node(10)
# l1.append(20)
# l1.append(30)
# l1.append(5)
# l1.display()
# l1.bubble()
# l1.display()

#Merge Sort in linked list
# def addTwoNumbers(s):
#     temp2=ListNode()
#     temp=temp2
#     c=0
#     while l1 or l2 or c:
#         s=c
#         if l1:
#             s+=l1.val
#             l1=l1.next
#             if l2:
#                 s+=l2.val
#                 l2=l2.next
#             c=s//10
#             temp.next=ListNode(s%10)
#             temp=temp.next
#         return temp2.next
#     print("None")
# 
# l1=Linked_list()
# l1.head=Node(10)
# l1.append(20)
# l1.append(30)
# l1.append(5)
# l1.display()
# l1.merge()
# l1.display()

#Remove letters from the string based on the numbers of stars
# l=[1,2,3,4,5]
# stack=[]
# for i in l:
#     stack.append(i)
# stack.pop()
# print(stack[-1])
# print(stack)

#Valid Parentheses: LeetCode problem
# def isValid(st):
#     st=[]
#     for i in s:
#         if i in "({[":
#             st.append(i)
#         else:
#             if not st:
#                 return False
#             l=st.pop()
#             if l=='(':
#                 if i!=')':
#                     return False
#             elif l=='{':
#                 if i!='}':
#                     return False
#             elif l=='[':
#                 if i!=']':
#                     return False
#     return not st
# 
# s="()[]{}"
# print(isValid(s))

#Removing the stars from a string: LeetCode Problem 
# def removeStars(s):
#         st=[]
#         for i in s:
#             if i=="*":
#                 if st:
#                     st.pop()
#             else:
#                 st.append(i)
#         return "".join(st)
# s = "leet**cod*e"
# print(removeStars(s))

#Number os students unable to eat lunch:1700-LeetCode Problem
# def countStudents(students,sandwiches):
#     c=len(students)
#     while students and sandwiches and sandwiches[0] in students:
#         if students[0]!=sandwiches[0]:
#             students.append(students[0])
#             students.pop(0)
#         else:
#             students.pop(0)
#             sandwiches.pop(0)
#             c-=1
#     return c
# 
# students=[1,1,1,0,0,1]
# sandwiches=[1,0,0,0,1,1]
# print(countStudents(students,sandwiches))
