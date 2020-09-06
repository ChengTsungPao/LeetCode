# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(p, q):
            if p == None and q == None:
                return True
            elif (p == None and q != None) or (p != None and q == None) or p.val != q.val:
                return False
            if not preorder(p.left, q.left):
                return False
            if not preorder(p.right, q.right):
                return False
            return True
        return preorder(p, q)