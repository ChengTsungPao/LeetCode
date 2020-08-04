class TreeNode:
    def __init__(self):
        self.val = False
        self.node = {}

class Trie:

    def __init__(self):
        self.trie = TreeNode()

    def insert(self, word: str) -> None:
        pointer = self.trie
        for ch in word:
            if ch not in pointer.node:
                pointer.node[ch] = TreeNode()
            pointer = pointer.node[ch]
        pointer.val = True
        
    def search(self, word: str) -> bool:
        pointer = self.trie
        for ch in word:
            if ch not in pointer.node:
                return False
            pointer = pointer.node[ch]
        return pointer.val
        
    def startsWith(self, prefix: str) -> bool:
        pointer = self.trie
        for ch in prefix:
            if ch not in pointer.node:
                return False
            pointer = pointer.node[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)