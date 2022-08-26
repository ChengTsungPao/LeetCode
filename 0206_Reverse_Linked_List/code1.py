# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prevNode = None
        node = head
        while node:
            temp = node.next
            node.next = prevNode
            prevNode = node
            node = temp
            
        return prevNode