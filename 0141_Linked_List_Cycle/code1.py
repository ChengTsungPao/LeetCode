# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head==None): return False
        mem = set()
        while(1):
            mem.add(id(head))
            if(head.next==None): return False            
            if(id(head.next) in mem):
                return True
            else:
                head = head.next
                