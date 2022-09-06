"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        ans = []
        
        def dfs(node, level):
            if not node:
                return
            
            if level >= len(ans):
                ans.append([])
                
            ans[level].append(node.val)
            
            for nextNode in node.children:
                dfs(nextNode, level + 1)
                
        dfs(root, 0)
        return ans