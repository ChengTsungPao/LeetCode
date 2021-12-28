# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        count = 0
        
        nums = set(nums)
        
        pointer = head
        sameHead = False
        
        while pointer:
            
            if sameHead and pointer.val in nums:
                pass
            elif sameHead == False and pointer.val in nums:
                count += 1
                sameHead = True
            else:
                sameHead = False
                
            pointer = pointer.next
        
        return count
        