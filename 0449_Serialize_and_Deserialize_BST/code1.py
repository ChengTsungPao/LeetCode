# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        
        def recur(root, index):
            nonlocal str_
            
            if not root:
                str_ += str(index) + "," + str(-1) + ","
                return
            str_ += str(index) + "," + str(root.val) + ","
            recur(root.left,  index * 2)
            recur(root.right, index * 2 + 1)
            
        str_ = ""    
        recur(root, 1)
        return str_[:-1]
    

    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        heap = {int(index) : int(val) for index, val in zip(data[0::2], data[1::2])}
        
        def recur(index):
            if heap[index] < 0:
                return None
            root = TreeNode(heap[index])
            root.left = recur(index * 2)
            root.right = recur(index * 2 + 1)
            return root
        
        return recur(1)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans