class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        pointer = self.trie
        for ch in word:
            if ch not in pointer:
                pointer[ch] = {}
            pointer = pointer[ch]   
        pointer["bool"] = True

    def search(self, word: str) -> bool:
        pointer = self.trie
        for ch in word:
            if ch not in pointer:
                return False
            pointer = pointer[ch]
        return "bool" in pointer      

    def startsWith(self, prefix: str) -> bool:
        pointer = self.trie
        for ch in prefix:
            if ch not in pointer:
                return False
            pointer = pointer[ch]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)