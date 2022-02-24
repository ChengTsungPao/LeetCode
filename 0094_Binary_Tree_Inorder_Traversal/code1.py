# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def inorder(node):
            if(node == None): 
                return None
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        return ans