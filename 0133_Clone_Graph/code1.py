"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        cache = {}
        
        def dfs(node):
            if not node:
                return None
            
            if id(node) in cache:
                return cache[id(node)]
            
            newNode = Node(node.val)
            cache[id(node)] = newNode
            for nextNode in node.neighbors:
                newNode.neighbors.append(dfs(nextNode))
                
            return newNode
                
        return dfs(node)