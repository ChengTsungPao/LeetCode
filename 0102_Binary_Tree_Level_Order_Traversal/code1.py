# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def preorder(node, index):
            if(node == None):
                return None
            elif(len(ans)-1 < index):
                ans.append([])
            ans[index].append(node.val)
            preorder(node.left, index + 1)
            preorder(node.right, index + 1)
        preorder(root, 0)
        return ans