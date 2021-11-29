# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def recur(node):
            
            if len(to_delete) == 0:
                return node
            
            if node == None:
                return None
            
            node.left = recur(node.left)
            node.right = recur(node.right)
            
            if node.val in to_delete:
                
                if node.left != None:
                    ans.append(node.left)
                    
                if node.right != None:
                    ans.append(node.right)
                    
                to_delete.remove(node.val)
                    
                return None
            
            return node
        
        to_delete = set(to_delete)
        
        ans = []
        
        if recur(root) != None:
            ans.append(root)
        
        return ans