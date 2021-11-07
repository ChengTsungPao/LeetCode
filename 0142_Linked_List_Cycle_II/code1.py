# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return None
        
        slow = head.next
        quick = head.next.next
        while quick and quick.next and slow != quick:
            slow = slow.next
            quick = quick.next.next 
            
        if slow != quick:
            return None
        
        newSlow = head
        while newSlow != slow:
            slow = slow.next
            newSlow = newSlow.next
            
        return slow