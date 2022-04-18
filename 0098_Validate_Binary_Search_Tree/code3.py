# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        preVal = -float("inf")
        while root:
            if not root.left:
                if preVal >= root.val:
                    return False
                preVal = root.val                
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if predecessor.right != root:
                    predecessor.right = root
                    root = root.left
                else:
                    predecessor.right = None
                    if preVal >= root.val:
                        return False
                    preVal = root.val
                    root = root.right
                
        return True