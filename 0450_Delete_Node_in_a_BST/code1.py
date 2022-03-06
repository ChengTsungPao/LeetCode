# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BST:
    def __init__(self, root):
        self.root = root
        
    def delete(self, val):

        def _delete(root, val):
            if not root:
                return None

            if val < root.val:
                root.left = _delete(root.left, val)
            elif val > root.val:
                root.right = _delete(root.right, val)
            else:
                # left child or right child is None
                if root.left == None:
                    tempNode = root.right
                    root.right = None
                    return tempNode
                elif root.right == None:
                    tempNode = root.left
                    root.left = None
                    return tempNode

                # left child and right child is not None
                # find left tree max value node
                tempNode = root.left
                while tempNode.right:
                    tempNode = tempNode.right
                root.val = tempNode.val
                root.left = _delete(root.left, tempNode.val)

            return root

        self.root = _delete(self.root, val)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        bst = BST(root)
        bst.delete(key)
        return bst.root