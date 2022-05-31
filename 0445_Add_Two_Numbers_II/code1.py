# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            preNode = None
            pointer = head
            while pointer:
                temp = pointer.next
                pointer.next = preNode
                preNode = pointer
                pointer = temp
            return preNode
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        dummy = ListNode()
        pointer = dummy
        carry = 0
        while l1 and l2:
            pointer.next = ListNode()
            pointer = pointer.next
            value = l1.val + l2.val + carry
            carry = value // 10
            pointer.val = value % 10            
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            pointer.next = ListNode()
            pointer = pointer.next
            value = l1.val + carry
            carry = value // 10
            pointer.val = value % 10
            l1 = l1.next
            
        while l2:
            pointer.next = ListNode()
            pointer = pointer.next
            value = l2.val + carry
            carry = value // 10
            pointer.val = value % 10
            l2 = l2.next
            
        if carry:
            pointer.next = ListNode()
            pointer = pointer.next
            pointer.val = carry
            
        return reverse(dummy.next)