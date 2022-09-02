class Node:
    def __init__(self, count = -1, keys = set(), left = None, right = None):
        self.left = left
        self.right = right
        self.count = count
        self.keys = keys
        
class DoubleLinkedList:
    def __init__(self):
        self.dummyHead = Node()
        self.dummyTail = Node()
        self.dummyHead.right = self.dummyTail
        self.dummyTail.left  = self.dummyHead

    def insert(self, node, key, count):
        leftNode, rightNode = node, node.right
        insertNode = Node(count, {key})
        
        leftNode.right = insertNode
        insertNode.left = leftNode
        insertNode.right = rightNode
        rightNode.left = insertNode
        return insertNode
        
    def update(self, node, key):
        node.keys.add(key) 
        return node
        
    def remove(self, node):
        leftNode = node.left
        rightNode = node.right
        leftNode.right = rightNode
        rightNode.left = leftNode
        del node
        
class AllOne:
    def __init__(self):
        self.dll = DoubleLinkedList()
        self.address = {}
        
    def inc(self, key: str) -> None:
        node = self.address[key] if key in self.address else self.dll.dummyHead
        count = node.count + 1 if node.count > 0 else 1

        if node.right.count == count:
            newNode = self.dll.update(node.right, key)
        else:
            newNode = self.dll.insert(node, key, count)  
        self.address[key] = newNode
        
        node.keys -= {key}
        if len(node.keys) == 0 and node.count > 0:
            self.dll.remove(node)

    def dec(self, key: str) -> None:
        node = self.address[key]
        count = node.count - 1
        
        if count > 0:
            if node.left.count == count:
                newNode = self.dll.update(node.left, key)
            else:
                newNode = self.dll.insert(node.left, key, count) 
            self.address[key] = newNode
        else:
            del self.address[key]
            
        node.keys -= {key}
        if len(node.keys) == 0 and node.count > 0:
            self.dll.remove(node)

    def getMaxKey(self) -> str:
        node = self.dll.dummyTail.left
        key = ""
        if node.count > 0:
            key = node.keys.pop()
            node.keys.add(key)
        return key 
        
    def getMinKey(self) -> str:
        node = self.dll.dummyHead.right
        key = ""
        if node.count > 0:
            key = node.keys.pop()
            node.keys.add(key)
        return key        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()