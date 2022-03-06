# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BST:
    def __init__(self, root):
        self.root = root
        
    def search(self, val):
        node = self.root
        while node and val != node.val:
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return node

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        bst = BST(root)
        return bst.search(val)