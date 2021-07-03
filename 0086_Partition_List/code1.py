# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        leftHead = ListNode()
        rightHead = ListNode()
        
        leftTail = leftHead    
        rightTail = rightHead
        
        pointer = head
        while pointer:
            temp = pointer
            if temp.val < x:
                leftTail.next = temp
                leftTail = leftTail.next
            elif temp.val >= x:
                rightTail.next = temp
                rightTail = rightTail.next
            pointer = pointer.next
            
        leftTail.next = None
        rightTail.next = None
            
        leftTail.next = rightHead.next
        
        return leftHead.next
