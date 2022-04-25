"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        que = collections.deque([root])
        while que:
            
            newQue = collections.deque()
            while que:
                node = que.pop()
                
                if que:
                    node.next = que[-1]
                    
                for nextNode in [node.left, node.right]:
                    if not nextNode:
                        continue
                        
                    newQue.appendleft(nextNode)
                    
            que = newQue.copy()
            
        return root 