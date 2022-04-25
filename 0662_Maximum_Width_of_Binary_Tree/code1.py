# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        indices = []
        def recur(root, level, index):
            if not root:
                return
            
            if level >= len(indices):
                indices.append([float("inf"), -float("inf")])
                
            indices[level][0] = min(indices[level][0], index)
            indices[level][1] = max(indices[level][1], index)
            
            recur(root.left, level + 1, 2 * index)
            recur(root.right, level + 1, 2 * index + 1)
            
        recur(root, 0, 1)

        ans = 1
        for left, right in indices:
            ans = max(ans, right - left + 1)
            
        return ans