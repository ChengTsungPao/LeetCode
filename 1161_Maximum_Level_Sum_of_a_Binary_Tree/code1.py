# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ans = (float("inf"), float("inf"))
        level = 1
        
        stack = [root]
        while stack:
            
            levelSum = 0
            newStack = []
            while stack:
                node = stack.pop()
                
                levelSum += node.val
                
                for nextNode in [node.left, node.right]:
                    if not nextNode:
                        continue
                        
                    newStack.append(nextNode)
                    
            ans = min(ans, (-levelSum, level))
            
            stack = newStack
            level += 1
            
        return ans[1]