# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = root
        
        def dfs(root):
            nonlocal ans
            
            if not root:
                return 0
            
            ret = dfs(root.left) + dfs(root.right)
            if root.val == p.val:
                ret += 1
            if root.val == q.val:
                ret += 1
            
            if ret == 2:
                ans = root
                return 0
            else:
                return ret
            
        dfs(root)
        return ans