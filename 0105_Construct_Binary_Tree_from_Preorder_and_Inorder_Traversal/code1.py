# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recur(i, j):
            nonlocal preorderIndex
            
            if i > j:
                return
            
            root_val = preorder[preorderIndex]
            root = TreeNode(root_val)
            preorderIndex += 1
            
            if i == j:
                return root
                        
            root.left = recur(i, index[root_val] - 1)
            root.right = recur(index[root_val] + 1, j)

            return root
        
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        
        preorderIndex = 0
        
        return recur(0, len(preorder) - 1)
        