# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(num, dp = {}):
            if str(num) not in dp:
                if len(num) == 0:
                    return [None] * (n != 0)
                dp[str(num)] = []
                for i in range(len(num)):
                    for left in dfs(num[:i], dp):
                        for right in dfs(num[i + 1:], dp):
                            dp[str(num)] += [TreeNode(num[i], left, right)]
            return dp[str(num)]
        return dfs(list(range(1, n + 1)))