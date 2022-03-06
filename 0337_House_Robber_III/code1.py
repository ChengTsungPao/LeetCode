# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}
        
        def recur(root, visited):
            
            if (id(root), visited) not in memo:
            
                if not root:
                    return 0
            
                if visited:
                    noLeftVisited = recur(root.left, not visited)
                    noRightVisited = recur(root.right, not visited)

                    ans = root.val + noLeftVisited + noRightVisited
                else:
                    leftVisited = recur(root.left, visited)
                    rightVisited = recur(root.right, visited)
                    noLeftVisited = recur(root.left, not visited)
                    noRightVisited = recur(root.right, not visited)

                    ans = max(leftVisited + rightVisited, \
                              leftVisited + noRightVisited, \
                              noLeftVisited + rightVisited, \
                              noLeftVisited + noRightVisited)

                memo[id(root), visited] = ans
            
            return memo[id(root), visited]
        
        return max(recur(root, True), recur(root, False))