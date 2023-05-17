# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # find mid pointer
        slow, quick = head, head.next
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            
        # reverse half linked list
        mid = slow
        preNode, pointer = head, head.next
        while id(preNode) != id(mid):
            nextNode = pointer.next
            pointer.next = preNode
            head.next = nextNode
            preNode = pointer
            pointer = nextNode
            
        # two pointer find max twin
        ans = 0
        left, right = preNode, pointer
        while id(left) != id(pointer):
            ans = max(ans, left.val + right.val)
            left, right = left.next, right.next
        
        return ans