# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def recur(node):
            if node == None:
                return 0
            
            return recur(node.left) + recur(node.right) + 1
        
        return recur(root)