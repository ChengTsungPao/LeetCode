# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def posorder(node):
            nonlocal maxnum
            if(node == None):
                return None            
            posorder(node.left)
            posorder(node.right)            
            if(node.left != None and node.right != None):
                maxnum = max(maxnum, node.left.val + node.right.val)
                node.val = max(node.left.val + 1, node.right.val + 1)
            elif(node.left != None):
                maxnum = max(maxnum, node.left.val)
                node.val = node.left.val + 1
            elif(node.right != None):
                maxnum = max(maxnum, node.right.val)
                node.val = node.right.val + 1
            else:
                node.val = 1

        maxnum = 0
        posorder(root)        
        return maxnum