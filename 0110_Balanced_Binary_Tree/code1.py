# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if node == None:
                return None
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            if node.right == None and node.left == None:
                node.val = 1
            elif node.right != None and node.left == None:
                if node.right.val > 1:
                    return True
                node.val = node.right.val + 1
            elif node.right == None and node.left != None:
                if node.left.val > 1:
                    return True
                node.val = node.left.val + 1
            else:
                if abs(node.left.val - node.right.val) > 1:
                    return True
                node.val = max(node.right.val, node.left.val) + 1
        if dfs(root):
            return False
        else:
            return True