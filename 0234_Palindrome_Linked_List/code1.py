# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # 龜兔賽跑找mid
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse mid ~ end
        mid = slow
        curHead = None
        while mid:   # 記住next_node，把自己往後丟指向curHead
            next_node = mid.next
            mid.next = curHead
            curHead = mid
            mid = next_node
        
        # compare
        mid = curHead
        while mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
            
        return True