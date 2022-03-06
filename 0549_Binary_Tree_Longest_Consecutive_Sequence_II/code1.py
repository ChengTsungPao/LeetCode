# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        ans = -float("inf")
        
        def recur(root, preVal):
            nonlocal ans
            
            if not root:
                return 0, 0
            
            leftIncrease, leftDecrease = recur(root.left, root.val)
            rightIncrease, rightDecrease = recur(root.right, root.val)
            
            ans = max(ans, leftIncrease + rightDecrease + 1, leftDecrease + rightIncrease + 1)
            
            increase = max(leftIncrease, rightIncrease) + 1
            decrease = max(leftDecrease, rightDecrease) + 1
            if preVal - 1 != root.val:
                increase = 0
            if preVal + 1 != root.val:
                decrease = 0

            return increase, decrease
        
        recur(root, float("inf"))
        
        return ans