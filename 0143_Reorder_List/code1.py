# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 龜兔賽跑找中間
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        
        # 反轉
        preNode = None
        midPointer = mid
        while midPointer:
            temp = midPointer.next 
            midPointer.next = preNode
            preNode = midPointer
            midPointer = temp
            
        # 合併  
        mid = preNode
        pointer = head
        while pointer and mid:
            temp = pointer.next
            pointer.next = mid
            mid = mid.next
            
            pointer.next.next = temp
            pointer = pointer.next.next
            
        return head