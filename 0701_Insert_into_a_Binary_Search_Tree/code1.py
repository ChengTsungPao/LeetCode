# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BST:
    def __init__(self, root):
        self.root = root
        
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        
        node = self.root
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        bst = BST(root)
        bst.insert(val)
        return bst.root