# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        head = ListNode()

        if l1.val < l2.val:
            head.val = l1.val
            l1 = l1.next
        else:
            head.val = l2.val
            l2 = l2.next

        temp = head

        while l1 and l2:
            temp.next = ListNode()

            if l1.val < l2.val:
                temp.next.val = l1.val
                l1 = l1.next
            else:
                temp.next.val = l2.val
                l2 = l2.next

            temp = temp.next

        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        else:
            temp.next = None

        return head
        