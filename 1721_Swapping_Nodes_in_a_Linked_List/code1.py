# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # get linked list length
        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next
        
        # get kth node
        start_kth_node = head
        for _ in range(k - 1):
            start_kth_node = start_kth_node.next
            
        end_kth_node = head
        for _ in range(length - k):
            end_kth_node = end_kth_node.next
        
        # swapping
        start_kth_node.val, end_kth_node.val = end_kth_node.val, start_kth_node.val

        return head