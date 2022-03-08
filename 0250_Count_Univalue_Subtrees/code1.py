# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def recur(root, preVal):
            if not root:
                return 0, True
            
            leftCount, leftVaild = recur(root.left, root.val)
            rightCount, rightVaild = recur(root.right, root.val)
            
            vaild = False
            count = leftCount + rightCount
            if leftVaild and rightVaild:
                count += 1
                vaild = True
                
            return count, vaild and preVal == root.val
        
        return recur(root, float("inf"))[0]