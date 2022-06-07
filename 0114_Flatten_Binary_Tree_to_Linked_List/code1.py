# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def recur(node):
            if not node:
                return None, None
            
            leftHead, leftTail = recur(node.left)
            rightHead, rightTail = recur(node.right)
            
            node.left = None
            if leftHead and rightHead:
                node.right = leftHead
                leftTail.right = rightHead
                head, tail = node, rightTail
            elif leftHead:
                node.right = leftHead
                head, tail = node, leftTail
            elif rightHead:
                node.right = rightHead
                head, tail = node, rightTail
            else:
                head, tail = node, node
                
            return head, tail
        
        return recur(root)[0]