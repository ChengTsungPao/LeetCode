# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

	# create double linked list        
        pointer = head
        while pointer.next:
            pointer.next.prev = pointer
            pointer = pointer.next
        
	# two pointer find max twin
        ans = 0
        left, right = head, pointer
        while id(left.next) != id(right):
            ans = max(ans, left.val + right.val)
            left, right = left.next, right.prev
        ans = max(ans, left.val + right.val)
        
        return ans