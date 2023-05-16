# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        preNode, pointer = dummy, dummy.next
        
        while pointer and pointer.next:
            preNode.next = pointer.next
            pointer.next = pointer.next.next
            preNode.next.next = pointer
            
            preNode = pointer
            pointer = pointer.next
            
        return dummy.next 