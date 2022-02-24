# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        node = root
        while node:
            if not node.left:
                ans.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right

                if predecessor.right != node:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    ans.append(node.val)
                    node = node.right

        return ans