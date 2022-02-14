# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def getOrder(root):
            stack = []
            preorder = ""
            direction = ""
            
            while stack or root:
                if root:
                    stack.append(root)
                    preorder += str(root.val) + "_"
                    direction += "L"
                    root = root.left
                else:
                    root = stack.pop()
                    direction += "R"
                    root = root.right
                    
            return preorder + "#" + direction
        
        def dfs(root):            
            if not root:
                return None
            
            sameTree[getOrder(root)].append(root)
                
            dfs(root.left)
            dfs(root.right)
        
        sameTree = collections.defaultdict(list)
        dfs(root)

        ans = []
        for tree in sameTree.keys():
            if len(sameTree[tree]) >= 2:
                ans.append(sameTree[tree][0])
        
        return ans