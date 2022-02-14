# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def reverseLinkedList(head):
            preNode = None
            curNode = head
            while curNode:
                temp = curNode.next
                curNode.next = preNode
                preNode = curNode
                curNode = temp
            return preNode
                
        head = reverseLinkedList(head)
        
        node = head
        while node:
            if node.val == 9:
                node.val = 0
                if not node.next:
                    node.next = ListNode()
                node = node.next
            else:
                node.val += 1
                break
                
        head = reverseLinkedList(head)
        
        return head