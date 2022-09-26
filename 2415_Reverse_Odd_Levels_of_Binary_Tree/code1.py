# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        level = 0
        que = collections.deque([root])
        while que:
            next_que = collections.deque()
            
            if level % 2 == 1:
                for node, value in zip(que, reversed([node.val for node in que])):
                    node.val = value
            
            for node in que:
                if node.left:
                    next_que.appendleft(node.left)
                if node.right:
                    next_que.appendleft(node.right)        
            
            que = next_que
            level += 1
            
        return root