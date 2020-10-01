# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        ans = [(-1, -1), (-2, -2)]
        def dfs(node, depth, source):
            if node == None:
                return None
            elif node.val == x or node.val == y:
                ans[ans[0][0] != -1] = (depth, source)
                return ans[1][0] != -2
            if dfs(node.left, depth + 1, node.val):
                return True
            if dfs(node.right, depth + 1, node.val):
                return True
        dfs(root, 0, -1)
        return ans[0][0] == ans[1][0] and ans[0][1] != ans[1][1]