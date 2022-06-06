# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        
        oddPointer  = head
        evenPointer = head.next
        evenHead    = head.next
        
        while oddPointer.next and evenPointer.next:
            oddPointer.next = oddPointer.next.next
            oddPointer = oddPointer.next

            evenPointer.next = evenPointer.next.next
            evenPointer = evenPointer.next

        oddPointer.next = evenHead
        
        return head