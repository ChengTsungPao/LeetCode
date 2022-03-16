# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root, ans, level):
            if not root:
                return
            
            if len(ans) <= level:
                ans.append(collections.deque())
                
            if level % 2 == 0:
                ans[level].append(root.val)
            else:
                ans[level].appendleft(root.val)
                
            dfs(root.left, ans, level + 1)
            dfs(root.right, ans, level + 1)
        
        ans = []
        dfs(root, ans, 0)
        
        return ans 