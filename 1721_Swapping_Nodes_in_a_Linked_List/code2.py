# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # get linked list length
        dummy = ListNode(0, head)
        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next
        
        # get kth node
        start_kth_preNode = dummy
        for _ in range(k - 1):
            start_kth_preNode = start_kth_preNode.next
        
        end_kth_preNode = dummy
        for _ in range(length - k):
            end_kth_preNode = end_kth_preNode.next
            
        start_kth_node = start_kth_preNode.next
        end_kth_node = end_kth_preNode.next
        
        if id(start_kth_node) == id(end_kth_node):
            return head
        
        # swapping
        start_kth_preNode.next = end_kth_node
        end_kth_preNode.next = start_kth_node
        
        temp = end_kth_node.next
        end_kth_node.next = start_kth_node.next
        start_kth_node.next = temp

        return dummy.next