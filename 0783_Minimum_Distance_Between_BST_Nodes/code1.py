# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        ans = float("inf")
        preVal = -float("inf")
        
        node = root
        while node:
            if not node.left:
                ans = min(ans, node.val - preVal)
                preVal = node.val
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                    
                if predecessor.right != node:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    ans = min(ans, node.val - preVal)
                    preVal = node.val
                    node = node.right
                    
        return ans