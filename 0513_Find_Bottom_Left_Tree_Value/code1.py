# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        ans = -1
        maxDepth = -1
        def dfs(root, depth):
            nonlocal ans, maxDepth
            
            if not root:
                return
            
            if depth > maxDepth:
                ans = root.val
                maxDepth = depth
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        return ans