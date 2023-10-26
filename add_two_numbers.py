# https://leetcode.com/problems/add-two-numbers2/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2
        carry = 0
        res = 0
        Head = None
        N = None

        while t1 and t2:  
            res = t1.val + t2.val + carry
            carry = int(res/10)
            res = res % 10

            if Head:
                N.next = ListNode(res)
                N = N.next
            else:
                Head = ListNode(res)
                N = Head
            t1 = t1.next
            t2 = t2.next
        
        while t1:
            
            res = t1.val  + carry
            carry = int(res/10)
            res = res % 10

            N.next = ListNode(res)
            t1 = t1.next
            N = N.next
        
        while t2:
            res =  t2.val + carry
            carry = int(res/10)
            res = res % 10
            
            N.next = ListNode(res)
            t2 = t2.next
            N = N.next
        if carry:
            N.next = ListNode(carry)
    
        return Head