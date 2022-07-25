# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer = head
        while pointer:
            while pointer.next and pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            pointer = pointer.next
            
        return head