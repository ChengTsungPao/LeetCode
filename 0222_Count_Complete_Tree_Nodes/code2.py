# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def recur(node, h):
            nonlocal count
            
            if node == None:
                if height == h:
                    return True
                else:
                    count += 1
                    return False
            
            if recur(node.right, h + 1) or recur(node.left, h + 1):
                return True
                
        height = 0
        node = root
        while node:
            height += 1
            node = node.left
        
        count = 0
        recur(root, 0)
        
        return 2 ** height - 1 - count