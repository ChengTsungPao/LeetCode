# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        pointer = head
        while pointer:
            pointer = pointer.next
            length += 1
        
        ans = []
        pointer = head
        q, r = length // k, length % k
        for _ in range(k):
            if q <= 0 and r <= 0:
                ans.append(None)
                continue
            
            newHead = pointer
            for _ in range(q + (r > 0)):
                preNode = pointer
                pointer = pointer.next
            preNode.next = None
            ans.append(newHead)
            r -= 1
            
        return ans
        