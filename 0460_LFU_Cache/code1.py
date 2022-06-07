class Node:
    def __init__(self, frequence = 0):
        self.LRUCache = LRUCache()
        self.frequence = frequence
        self.leftNode = None
        self.rightNode = None

class LFUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.keyFrequence = collections.defaultdict(int)
        self.frequenceNode = {0: self.head}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keyFrequence:
            return -1
        frequence = self.keyFrequence[key]
        node = self.frequenceNode[frequence]
        value = node.LRUCache.get(key)
        self.updateFrequence(key, value)
        return value
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        if key not in self.keyFrequence and len(self.keyFrequence) == self.capacity:
            self.removeSmallerFrequence()
        self.updateFrequence(key, value)
            
    def updateFrequence(self, key, value):
        frequence = self.keyFrequence[key]
        node = self.frequenceNode[frequence]
        
        # update linkedList
        if frequence > 0:
            node.LRUCache.remove(key)
            
        if not node.rightNode or node.rightNode.frequence != frequence + 1:
            newNode = Node(frequence + 1)
            self.insertNode(node, newNode)
        node = node.rightNode
        node.LRUCache.put(key, value)
        
        if node.leftNode.frequence > 0 and node.leftNode.LRUCache.getLength() == 0:
            self.deleteNode(node.leftNode)
            del self.frequenceNode[frequence]
            
        # update hash table
        self.keyFrequence[key] = frequence + 1
        self.frequenceNode[frequence + 1] = node
        
    def removeSmallerFrequence(self):
        node = self.head.rightNode
        key, value = node.LRUCache.popitems()
        frequence = self.keyFrequence[key]
        del self.keyFrequence[key]
        if node.LRUCache.getLength() == 0:
            self.deleteNode(node)
            del self.frequenceNode[frequence]
            
    def insertNode(self, node, newNode):
        left, right = node, node.rightNode
        left.rightNode = newNode
        newNode.leftNode = left
        newNode.rightNode = right
        if right: right.leftNode = newNode

    def deleteNode(self, node):
        left = node.leftNode
        right = node.rightNode
        left.rightNode = right
        if right: right.leftNode = left
        del node

class LRUCache:
    def __init__(self):
        self.cache = collections.OrderedDict()
        
    def get(self, key: int) -> int:
        value = self.cache[key]
        self.cache.move_to_end(key)
        return value
        
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        
    def popitems(self):
        return self.cache.popitem(last = False)
        
    def remove(self, key):
        del self.cache[key]
        
    def getLength(self):
        return len(self.cache)

        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)