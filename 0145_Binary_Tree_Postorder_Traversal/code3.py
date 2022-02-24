# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        node = root
        while node:
            if not node.right:
                ans.append(node.val)
                node = node.left
            else:
                predecessor = node.right
                while predecessor.left and predecessor.left != node:
                    predecessor = predecessor.left

                if predecessor.left != node:
                    ans.append(node.val)
                    predecessor.left = node
                    node = node.right
                else:
                    predecessor.left = None
                    node = node.left

        return ans[::-1]