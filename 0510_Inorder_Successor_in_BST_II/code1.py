"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
        else:
            successor = node.parent
            while successor and successor.left != node:
                successor = successor.parent
                node = node.parent
            
        return successor