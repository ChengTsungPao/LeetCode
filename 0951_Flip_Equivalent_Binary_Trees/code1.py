# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def compare(node1, node2):
            if node1 == None and node2 == None:
                return True
            elif node1 != None and node2 == None:
                return False
            elif node1 == None and node2 != None:
                return False
            elif node1.val == node2.val:
                return True
            else:
                return False
            
        def dfs(node1, node2):
            
            if node1 == None and node2 == None:
                return True
            elif node1 != None and node2 == None:
                return False
            elif node1 == None and node2 != None:
                return False
            
            if compare(node1.left, node2.left):
                if dfs(node1.left, node2.left) and compare(node1.right, node2.right):
                    return dfs(node1.right, node2.right)
                else:
                    return False
            elif compare(node1.left, node2.right):
                if dfs(node1.left, node2.right) and compare(node1.right, node2.left):
                    return dfs(node1.right, node2.left)
                else:
                    return False
            else:
                return False
            
        return compare(root1, root2) and dfs(root1, root2)
