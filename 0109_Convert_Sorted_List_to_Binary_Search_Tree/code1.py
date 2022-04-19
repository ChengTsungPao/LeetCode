# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def findMedian(head):
            preNode = slow = quick = head
            while quick and quick.next:
                preNode = slow
                slow = slow.next
                quick = quick.next.next
            preNode.next = None
            return slow
        
        def recur(head):
            if not head:
                return None
            elif not head.next:
                return TreeNode(head.val)

            midNode = findMedian(head)
            root = TreeNode(midNode.val)
            root.left = recur(head)
            root.right = recur(midNode.next)
            
            return root
        
        return recur(head)     