# 阿寶
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        def recur(root):
            if not root:
                return None, None
            
            if root.val > target:
                smallerNode, biggerNode = recur(root.left)
                root.left = biggerNode
                return smallerNode, root
            else:
                smallerNode, biggerNode = recur(root.right)
                root.right = smallerNode
                return root, biggerNode
            
        return recur(root)