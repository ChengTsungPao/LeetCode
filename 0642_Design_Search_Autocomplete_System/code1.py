class Node:
    def __init__(self,  word = "", times = 0):
        self.children = {}
        self.times = times
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word, times):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.times += times
        node.isWord = True
        
    def search(self, prefixWord):
        node = self.root
        for ch in prefixWord:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        def _search(node, word):
            ret = [(-node.times, word)] if node.isWord else []
            for ch, nextNode in node.children.items():
                ret.extend(_search(nextNode, word + ch))
            return ret
        
        return _search(node, prefixWord)
    
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.currentWord = ""
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)
            
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.currentWord, 1)
            self.currentWord = ""
            return []
        
        self.currentWord += c
        
        ans = []
        heap = self.trie.search(self.currentWord)
        heapq.heapify(heap)
        for _ in range(3):
            if heap:
                times, word = heapq.heappop(heap)
                ans.append(word)
            else:
                break
        
        return ans