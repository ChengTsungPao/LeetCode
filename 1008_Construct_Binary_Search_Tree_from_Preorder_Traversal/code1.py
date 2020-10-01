# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(node, _list):
            if(len(_list) == 0):
                return None
            left, right = [], []
            for i in range(len(_list)):
                if(_list[i] < node.val):
                    left.append(_list[i])
                else:
                    right.append(_list[i])  
            if(len(left) >= 1):
                node.left = TreeNode(left[0])
                dfs(node.left, left[1:])
            if(len(right) >= 1):
                node.right = TreeNode(right[0])
                dfs(node.right, right[1:])
        root = TreeNode(preorder[0])
        dfs(root, preorder[1:])
        return root