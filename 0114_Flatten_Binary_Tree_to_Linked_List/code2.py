# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        node = root
        while node:
            if not node.left:
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                    
                if predecessor.right != node:
                    predecessor.right = node
                    node = node.left
                else:
                    temp = node.right
                    node.right = node.left
                    predecessor.right = temp
                    node.left = None
                    node = temp