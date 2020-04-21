# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        mindepth = float("inf")
        def dfs(node, index):
            nonlocal mindepth
            if(node == None):
                return None
            elif(node.left == None and node.right == None):
                mindepth = min(mindepth, index)
                return None
            elif(index >= mindepth):
                return None
            dfs(node.left, index + 1)
            dfs(node.right, index + 1)
        dfs(root, 1)
        if(root == None):
            return 0
        else:
            return mindepth