# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        while root:
            if not root.left:
                k -= 1
                if k == 0:
                    return root.val
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
                    k -= 1
                    if k == 0:
                        return root.val
                    root = root.right
                    
        return -1