# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = -1
        isFind = True
        
        def dfs(node):
            nonlocal ans, isFind
            
            if isFind == False:
                return 0
            
            if node == None:
                return 0

            ret = dfs(node.left) + dfs(node.right) + (node.val == p.val) + (node.val == q.val)
            if isFind and ret == 2:
                ans = node
                isFind = False
                
            return ret
        
        dfs(root)
        return ans