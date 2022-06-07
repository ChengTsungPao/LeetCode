"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node = head
        while node:
            if not node.child:
                node = node.next
            else:
                predecessor = node.child
                while predecessor.next and predecessor.next != node:
                    predecessor = predecessor.next
                    
                if predecessor.next != node:
                    predecessor.next = node
                    node = node.child
                else:         
                    temp = node.next
                    predecessor.next = temp
                    node.next = node.child
                    node.child = None
                    node = temp
                    
        node = head        
        while node and node.next:
            node.next.prev = node
            node = node.next
            
        return head