# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        ans = uDepth = None
        
        def dfs(node, depth):
            nonlocal ans, uDepth
            
            if not node:
                return False

            if uDepth == None and node == u:
                uDepth = depth
                return False
            elif uDepth == depth:
                ans = node
                return True

            return dfs(node.left, depth + 1) or dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return ans 