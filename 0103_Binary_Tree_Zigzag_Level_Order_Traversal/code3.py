# write code here
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        ans = []
        level = 0
        stack = [root]
        
        while stack:
            
            newStack = []
            while stack:
                node = stack.pop()
                
                if level >= len(ans):
                    ans.append([])
                ans[level].append(node.val)
                
                if level % 2 == 0:
                    if node.left:
                        newStack.append(node.left)
                    if node.right:
                        newStack.append(node.right)
                else:
                    if node.right:
                        newStack.append(node.right)
                    if node.left:
                        newStack.append(node.left)
                        
            level += 1
            stack = newStack

        return ans