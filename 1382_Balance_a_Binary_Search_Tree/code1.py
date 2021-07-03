# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if node == None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_array = inorder(root)
        
        def build(i, j):
            if i > j:
                return None
            cutIndex = (i + j) // 2
            node = TreeNode(sorted_array[cutIndex])
            node.left = build(i, cutIndex - 1)
            node.right = build(cutIndex + 1, j)
            return node
            
        return build(0, len(sorted_array) - 1)