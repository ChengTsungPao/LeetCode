# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        memo = {}
        
        def recur(n):
            
            if n not in memo:
                if n == 1:
                    return [TreeNode()]

                ans = []
                for i in range(1, n - 1):
                    for left in recur(i):
                        for right in recur(n - i - 1):
                            node = TreeNode()
                            node.left = left
                            node.right = right
                            ans.append(node)
                            
                memo[n] = ans

            return memo[n]
        
        return recur(n)