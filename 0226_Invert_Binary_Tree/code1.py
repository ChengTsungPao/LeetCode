# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node == None:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root