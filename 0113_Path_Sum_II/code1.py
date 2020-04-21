# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def dfs(node, _list, _sum):
            if(node.left == None and node.right == None):
                if(_sum == sum):
                    ans.append(_list)
                return None       
            if(node.left != None):
                dfs(node.left, _list + [node.left.val], _sum + node.left.val)
            if(node.right != None):
                dfs(node.right, _list + [node.right.val], _sum + node.right.val)
        if(root != None):
            dfs(root, [root.val], root.val)
        return ans
