class Node:
    def __init__(self):
        self.next = {}
        self.word = False
    
    
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.next:
                node.next[ch] = Node()
            node = node.next[ch]
        node.word = True
        
    def search(self, word):
        
        def _search(index, node, count):
            if index >= len(word):
                return node.word and count == 0
            
            ret = False
            for ch in node.next:
                if count > 0 and ch != word[index]:
                    ret = _search(index + 1, node.next[ch], count - 1)
                elif ch == word[index]:
                    ret = _search(index + 1, node.next[ch], count)
                if ret:
                    return True
                
            return False

        return _search(0, self.root, 1)
    
    
class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.add(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)