# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        key = ""
        que = collections.deque([root])
        while que:
            node = que.pop()
            
            if not node:
                key += ",#"
                continue
            
            key += "," + str(node.val)
            
            que.appendleft(node.left)
            que.appendleft(node.right)
        
        return key[1:]
        
        
    def deserialize(self, data):
        if data == "":
            return None
        
        arr = data.split(",")
        
        value = int(arr[0])
        head = TreeNode(value)
        index = 1
        
        que = collections.deque([head])
        while que:
            node = que.pop()
            
            if index < len(arr) and arr[index] != "#":
                value = int(arr[index])
                node.left = TreeNode(value)
                que.appendleft(node.left)
            index += 1

            if index < len(arr) and arr[index] != "#":
                value = int(arr[index])
                node.right = TreeNode(value)
                que.appendleft(node.right)
            index += 1
            
        return head


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))