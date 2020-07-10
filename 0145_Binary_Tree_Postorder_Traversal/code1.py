# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def postorder(node):
            if(node == None):
                return None
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)
        postorder(root)
        return ans 