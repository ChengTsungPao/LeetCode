# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        def insert(node, endNode):
            # get insert pos
            preNode = dummy
            pointer = dummy.next
            while pointer and id(pointer) != id(endNode) and pointer.val < node.val:
                preNode = pointer
                pointer = pointer.next
            
            # insert node
            temp = preNode.next
            preNode.next = node
            node.next = temp
        
        # insertion sort
        preNode = dummy
        pointer = dummy.next
        while pointer:
            node, endNode = pointer, pointer.next
            
            preNode.next = endNode
            node.next = None
            insert(node, endNode)
            
            pointer = endNode
            if id(preNode.next) != id(endNode):
                preNode = preNode.next
                
        return dummy.next