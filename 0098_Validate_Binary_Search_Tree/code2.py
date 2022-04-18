# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(root):            
            if not root:
                return float("inf"), -float("inf"), True
            
            leftMin, leftMax, isValid = recur(root.left)
            if isValid == False or root.val <= leftMax:
                return -1, -1, False
            
            rightMin, rightMax, isValid = recur(root.right)
            if isValid == False or root.val >= rightMin:
                return -1, -1, False
            
            return min(leftMin, root.val), max(rightMax, root.val), True
        
        return recur(root)[2]