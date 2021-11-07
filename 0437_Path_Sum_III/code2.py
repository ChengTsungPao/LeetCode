# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def recur(node, curSum):
            nonlocal ans
            
            if node == None:
                return 0
            
            curSum += node.val
            ans += preSum.get(curSum - targetSum, 0)
            
            preSum[curSum] = preSum.get(curSum, 0) + 1
            
            recur(node.left, curSum)
            recur(node.right, curSum)
            
            preSum[curSum] -= 1
        
        
        preSum = {0: 1}
        ans = 0
        recur(root, 0)
        
        return ans