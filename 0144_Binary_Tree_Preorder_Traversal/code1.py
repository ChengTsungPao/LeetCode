# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def preorder(node):
            if(node == None):
                return None
            else:
                ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ans