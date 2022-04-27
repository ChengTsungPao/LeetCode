# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        # 情況一: 1, 5, 3, 4, 2 => 1, 2, 3, 4, 5
        # 情況二: 1, 2, 4, 3, 5 => 1, 2, 3, 4, 5
        
        preNode = None
        wrongNode = []
        node = root
        
        while node:
            if not node.left:
                
                if preNode and preNode.val > node.val:
                    wrongNode.append((preNode, node))

                preNode = node
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
                    
                    if preNode and preNode.val > node.val:
                        wrongNode.append((preNode, node))
                    
                    preNode = node
                    node = node.right
     
        if len(wrongNode) == 1:
            node1, node2 = wrongNode[0]
        else:
            node1, node2 = wrongNode[0][0], wrongNode[1][1]
                
        node1.val, node2.val = node2.val, node1.val