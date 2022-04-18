# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        def recur(root):
            if not root:
                return 0
            
            left = recur(root.left)
            right = recur(root.right)
            
            height = max(left, right)
            if height >= len(ans):
                ans.append([])
            ans[height].append(root.val)
            
            return height + 1
        
        recur(root)
        return ans 