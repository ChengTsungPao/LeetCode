# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
            
        def reverseKNode(head, times):

            if times == 0:
                return head
            
            next_k_pointer = head
            for _ in range(k):
                next_k_pointer = next_k_pointer.next
                
            next_k_pointer = reverseKNode(next_k_pointer, times - 1)
            
            nexttemp = head.next
            head.next = next_k_pointer
            for _ in range(k - 1):
                temp = nexttemp.next
                nexttemp.next = head
                head = nexttemp
                nexttemp = temp
                
            return head
        
        length, pointer = 0, head
        
        while pointer:
            pointer = pointer.next
            length += 1
            
        times = length // k
        
        return reverseKNode(head, times)
