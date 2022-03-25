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
                return set()
            
            children = dfs(root.left) | dfs(root.right)
            children.add(root.val)
            
            if p.val in children and q.val in children:
                ans = root
                return set()
            else:
                return children
            
        dfs(root)
        return ans