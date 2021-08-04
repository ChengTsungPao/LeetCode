# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def dfs(node, targetSum):
            
            if node == None:
                return []
            elif node.left == None and node.right == None and targetSum == node.val:
                return [[node.val]]

            ans = []
            for i in dfs(node.left, targetSum - node.val):
                ans.append([node.val] + i)
            for i in dfs(node.right, targetSum - node.val):
                ans.append([node.val] + i)
                
            return ans
        
        return dfs(root, targetSum)
