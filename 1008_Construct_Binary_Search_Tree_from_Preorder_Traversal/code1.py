# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def recur(i, j):
            nonlocal preorderIndex
            
            if i > j:
                return
            
            root_val = preorder[preorderIndex]
            root = TreeNode(root_val)
            preorderIndex += 1
            
            if i == j:
                return root
            
            nextBiggerIndex = nextBiggerIndexDict.get(root_val, len(preorder))

            root.left = recur(i + 1, nextBiggerIndex - 1)
            root.right = recur(nextBiggerIndex, j)
            
            return root
        
        
        # monotonic stack => find next bigger val index
        stack, nextBiggerIndexDict = [], {}
        
        for i in range(len(preorder)):
            while stack and stack[-1] < preorder[i]:
                nextBiggerIndexDict[stack.pop()] = i
            stack.append(preorder[i])
        
        preorderIndex = 0
        
        return recur(0, len(preorder) - 1)