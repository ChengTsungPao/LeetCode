class Node:
    def __init__(self):
        self.children = {}
        self.frequence = 0
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
            node.frequence += 1
        node.isWord = True
        
    def search(self, word):
        n = len(word)
        node = self.root.children[word[0]]
        for index in range(1, n):
            ch = word[index]
            if node.frequence == 1:
                return index
            node = node.children[ch]
        return n
                
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        n = len(words)
        
        groups = collections.defaultdict(Trie)
        for word in words:
            groups[len(word), word[0], word[-1]].insert(word)
            
        ans = []
        for word in words:
            length, first, last = len(word), word[0], word[-1]
            p = groups[length, first, last].search(word)
            size = length - 1 - p
            if size > 1:
                ans.append(word[:p] + str(size) + last)
            else:
                ans.append(word)
                
        return ans