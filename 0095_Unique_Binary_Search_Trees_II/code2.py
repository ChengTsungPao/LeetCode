# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        memo = {}
        def recur(i, j):
            
            if (i, j) not in memo:
            
                if i > j:
                    return [None]
            
                ret = []
                for k in range(i, j + 1):
                    for left in recur(i, k - 1):
                        for right in recur(k + 1, j):
                            root = TreeNode(k)
                            root.left = left
                            root.right = right
                            ret.append(root)
                            
                memo[i, j] = ret
            
            return memo[i, j]
        
        return recur(1, n)