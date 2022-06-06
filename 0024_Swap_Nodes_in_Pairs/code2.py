# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        preNode = dummy = ListNode()
        evenPointer = head
        oddPointer  = head.next
        while oddPointer:
            temp = oddPointer.next
            evenPointer.next = temp
            oddPointer.next = evenPointer
            preNode.next = oddPointer
            
            if not temp:
                break
            preNode = evenPointer
            evenPointer = temp
            oddPointer  = temp.next
        
        return dummy.next