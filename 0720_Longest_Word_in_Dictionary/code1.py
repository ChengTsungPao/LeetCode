class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.tree = Node()
        self.tree.isWord = True
        
    def add(self, word):
        node = self.tree
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.isWord = True
        
    def search(self):
        
        def _search(node):
            ret = 0, ""
            for ch in node.children.keys():
                nextNode = node.children[ch]
                if nextNode.isWord == False:
                    continue
                
                word = ch + _search(nextNode)
                ret = min(ret, (-len(word), word))
            return ret[1]
        
        return _search(self.tree)
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        tree = Trie()

        for word in words:
            tree.add(word)
            
        return tree.search()