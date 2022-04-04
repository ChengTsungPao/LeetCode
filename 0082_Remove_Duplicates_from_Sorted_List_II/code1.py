# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        preNode = dummy
        pointer = head
        
        while pointer:
            value = pointer.val
            
            if pointer.next == None or pointer.next.val != value:
                preNode = pointer
                pointer = pointer.next
            else:
                while pointer and pointer.val == value:
                    pointer = pointer.next
                preNode.next = pointer
            
        return dummy.next