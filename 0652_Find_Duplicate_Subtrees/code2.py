# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:  
        
        ans = []
        treeDict = collections.defaultdict(int)
        
        def dfs(node):
            if not node:
                return "#"
            
            treeKey = "L" + dfs(node.left) + "R" + dfs(node.right) + "_" + str(node.val)
            
            if treeDict[treeKey] == 1:
                ans.append(node)
                
            treeDict[treeKey] += 1
            return treeKey
        
        dfs(root)
        return ans