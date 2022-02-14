# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        '''
        Inorder Traversal BST => Sorted Sequence
        1. 若找到的 root 比 p 還要大 => 代表 right tree 都不是 successor
        2. 若找到的 root 比 p 還要小 => 代表  left tree 都不是 successor
        '''
        
        successor = None
        
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
                
        return successor