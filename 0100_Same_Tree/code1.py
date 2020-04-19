# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(node):
            nonlocal _list
            if(node == None):
                return None
            else:
                _list.append(node.val)
            _list.append(0)
            dfs(node.left)
            _list.append(1)
            dfs(node.right)
            
        _list = []
        dfs(p)
        
        tmp = copy.copy(_list)
        _list = []
        dfs(q)
        
        if(tmp == _list):
            return True
        else:
            return False