# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        position = {}
        def dfs(node, i, j):
            if node == None:
                return None
            position[i, j, node.val] = node.val
            dfs(node.left, i - 1, j + 1)
            dfs(node.right, i + 1, j + 1)
        dfs(root, 0, 0)
        
        ans = []
        key = sorted(position.keys())
        for i in range(len(key)):
            if i == 0 or key[i][0] != key[i - 1][0]:
                ans.append([])
            ans[-1].append(position[key[i][0], key[i][1], key[i][2]])
        return ans