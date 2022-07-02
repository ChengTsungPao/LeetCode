# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(L1, L2):
            
            pointer = dummy = ListNode()
            while L1 and L2:
                if L1.val < L2.val:
                    pointer.next = L1
                    L1 = L1.next
                else:
                    pointer.next = L2
                    L2 = L2.next
                pointer = pointer.next
            
            if L1:
                pointer.next = L1
            if L2:
                pointer.next = L2   
                
            return dummy.next
        
        
        n = len(lists)
        
        length = 1
        while length < n:
            for index in range(0, n, length * 2):
                if index + length < n:
                    lists[index] = merge(lists[index], lists[index + length])
            length *= 2
        
        return lists[0] if lists else None