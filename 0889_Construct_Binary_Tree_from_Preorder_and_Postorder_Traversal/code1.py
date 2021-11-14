# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def recur(i, j):
            nonlocal preorderIndex
            
            if i > j:
                return
            
            root_val = preorder[preorderIndex]
            root = TreeNode(root_val)
            preorderIndex += 1
            
            if i == j:
                return root
            
            next_left_val = preorder[preorderIndex]
            root.left = recur(i, index[next_left_val])
            root.right = recur(index[next_left_val] + 1, j - 1)
            
            return root
        
        index = {}
        for i in range(len(postorder)):
            index[postorder[i]] = i
        
        preorderIndex = 0
        
        return recur(0, len(preorder) - 1)