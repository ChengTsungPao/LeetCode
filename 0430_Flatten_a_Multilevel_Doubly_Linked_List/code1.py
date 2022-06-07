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
        
        def recur(node):
            if not node:
                return None, None
            
            childHead, childTail = recur(node.child)
            nextHead, nextTail = recur(node.next)
            
            node.child = None
            if childHead and nextHead:
                node.next = childHead
                childHead.prev = node
                childTail.next = nextHead
                nextHead.prev = childTail
                head, tail = node, nextTail
            elif childHead:
                node.next = childHead
                childHead.prev = node
                head, tail = node, childTail
            elif nextHead:
                node.next = nextHead
                nextHead.prev = node
                head, tail = node, nextTail
            else:
                head, tail = node, node
                
            return head, tail
        
        return recur(head)[0]