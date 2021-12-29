# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def getRightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        def recur(node):
            if node == None:
                return 0
            
            leftHeight, rightHeight = getLeftHeight(node), getRightHeight(node)
            if leftHeight == rightHeight:
                return 2 ** leftHeight - 1
            else:
                return recur(node.left) + recur(node.right) + 1
        
        return recur(root)