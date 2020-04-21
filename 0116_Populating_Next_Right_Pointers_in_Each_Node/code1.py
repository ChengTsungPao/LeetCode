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
        if(root == None):
            return root
        que = collections.deque()
        que.append((root, 0))
        while que:
            if(que[-1][0].left != None):
                que.insert(0, (que[-1][0].left, que[-1][1] + 1))
            if(que[-1][0].right != None):
                que.insert(0, (que[-1][0].right, que[-1][1] + 1))
            if(len(que) >= 2 and que[-1][1] == que[-2][1]):
                que[-1][0].next = que[-2][0]
                que.pop()
            else:
                que.pop()[0].next = None
        return root  