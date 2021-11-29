# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        # 阿寶
        
        def dfs(node):
            nonlocal ans
            
            if node == None:
                return 0
            
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            
            if node.left == None or (node.left.val - node.val != 1):
                maxLeft = 0

            if node.right == None or (node.right.val - node.val != 1):
                maxRight = 0
            
            ret = max(maxLeft, maxRight) + 1
            ans = max(ans, ret)

            return ret
        
        ans = 0
        dfs(root)
        return ans