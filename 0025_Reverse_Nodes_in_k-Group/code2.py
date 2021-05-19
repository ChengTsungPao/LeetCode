# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if k == 1: return head
        
        length, pointer = 0, head
        
        while pointer:
            pointer = pointer.next
            length += 1

        emptytail = ListNode()
        emptytail.next = head
        times, count = length // k, 0
        curtail, curhead = emptytail, emptytail.next
        
        while times > 0:

            temp = curhead.next
            curhead.next = curhead.next.next
            temp.next = curtail.next
            curtail.next = temp
            
            count += 1
            
            if count % (k - 1) == 0:
                curtail, curhead = curhead, curhead.next
                times -= 1
            
        return emptytail.next