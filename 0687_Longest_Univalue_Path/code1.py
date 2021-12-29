# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def recur(node):
            nonlocal ans
            
            if node == None:
                return 0, None
            
            curNum = node.val
            
            leftCount, leftNum = recur(node.left)
            rightCount, rightNum = recur(node.right)
            
            if curNum == leftNum and curNum == rightNum:
                ans = max(ans, leftCount + rightCount + 1)
                return max(leftCount, rightCount) + 1, curNum
            elif curNum == leftNum:
                ans = max(ans, leftCount + 1)
                return leftCount + 1, curNum
            elif curNum == rightNum:
                ans = max(ans, rightCount + 1)
                return rightCount + 1, curNum
            else:
                return 1, curNum
            
        ans = 1
        recur(root)
        
        return ans - 1
        