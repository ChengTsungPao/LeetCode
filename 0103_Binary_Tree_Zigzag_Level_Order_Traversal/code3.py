# write code here
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        ans = []
        level = 0
        deque = collections.deque([root])

        while deque:
            
            newDeque = collections.deque()            
            while deque:
                node = deque.pop()
                
                if level % 2 == 0:
                    if node.left:
                        newDeque.append(node.left)
                    if node.right:
                        newDeque.append(node.right)
                elif level % 2 == 1:
                    if node.right:
                        newDeque.append(node.right) 
                    if node.left:
                        newDeque.append(node.left)
                        
                if len(ans) <= level:
                    ans.append([])
                ans[level].append(node.val)
                
            level += 1
            deque = newDeque.copy()

        return ans