# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def recur(i, j):
            nonlocal postorderIndex
            
            if i > j:
                return
            
            root_val = postorder[postorderIndex]
            root = TreeNode(root_val)
            postorderIndex -= 1
            
            if i == j:
                return root
            
            root.right = recur(index[root_val] + 1, j)
            root.left = recur(i, index[root_val] - 1)
            
            return root
            
        
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
            
        postorderIndex = len(postorder) - 1
        
        return recur(0, len(postorder) - 1)