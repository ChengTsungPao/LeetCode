# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.index = self.countTree(root) + 1
        
    def countTree(self, node):
        if not node:
            return 0
        return self.countTree(node.left) + self.countTree(node.right) + 1

    def insert(self, val: int) -> int:
        index = self.index
        
        direction = []
        while index > 1:
            if index % 2 == 0:
                direction.append("L")
            else:
                direction.append("R")
            index //= 2
        direction = direction[::-1]
            
        node = self.root
        for d in direction[:-1]:
            if d == "L":
                node = node.left
            else:
                node = node.right
        if direction[-1] == "L":
            node.left = TreeNode(val)
        else:
            node.right = TreeNode(val)

        self.index += 1
        return node.val
    
    def get_root(self) -> Optional[TreeNode]:
        return self.root
        

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()