"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeDict = {}
        
        copyNodeHead = Node(0)
        copyNodePointer = copyNodeHead
        
        while head:
            if id(head) not in nodeDict:
                copyNode = Node(head.val)
                nodeDict[id(head)] = copyNode
            else:
                copyNode = nodeDict[id(head)]
            
            if id(head.random) not in nodeDict:
                if head.random != None:
                    randomNode = Node(head.random.val)
                    nodeDict[id(head.random)] = randomNode
                else:
                    randomNode = None
            else:
                randomNode = nodeDict[id(head.random)]
                
            copyNodePointer.next = copyNode
            copyNodePointer.next.random = randomNode
            copyNodePointer = copyNodePointer.next
            head = head.next
        
        return copyNodeHead.next