# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        temp = head
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        temp = head
        for value in arr:
            temp.val = value
            temp = temp.next
        return head