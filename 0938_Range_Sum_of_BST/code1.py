# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        def dfs(node):
            if node == None:
                return 0
            return node.val * (low <= node.val <= high) + dfs(node.left) + dfs(node.right)
        
        return dfs(root)