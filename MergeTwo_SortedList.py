# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.H = None
        self.TN = None

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        while list1 and list2:
            if list1.val >= list2.val:
                self.add_val(list2)
                list2 = list2.next
            elif list2.val > list1.val:
                self.add_val(list1)
                list1 = list1.next
        
        while list1:
            self.add_val(list1)
            list1 = list1.next

        while list2:
            self.add_val(list2)
            list2 = list2.next
        # del self.TN
        return self.H

    def add_val(self,node):
        if self.H:
            self.TN.next = node
            self.TN = self.TN.next
        else:
            self.H = node
            self.TN = self.H