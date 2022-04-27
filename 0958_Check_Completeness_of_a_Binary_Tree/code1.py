# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        number = 0
        que = collections.deque([(root, 1)])
        
        while que:
            node, num = que.pop()
            
            number += 1
            if number != num:
                return False
            
            if node.left:
                que.appendleft((node.left, num * 2))
            if node.right:
                que.appendleft((node.right, num * 2 + 1))
                
        return True