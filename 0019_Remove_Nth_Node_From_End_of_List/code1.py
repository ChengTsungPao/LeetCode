# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        if length <= n:
            return head.next
        else:
            length -= n
            temp = head
            for _ in range(length - 1):
                temp = temp.next
            temp.next = temp.next.next
            return head 