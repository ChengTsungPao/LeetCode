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
        
    def search(self):
        
        ans = {}
        def _search(node, count, word):            
            if node.isWord:
                count -= 1
                ans[word] = word[:~count] + str(count) + word[-1] if count > 1 else word
                return
            
            for ch, childNode in node.children.items():
                _search(childNode, count + (node.frequence == 1), word + ch)
                    
        node, word = self.root, ""
        for ch, childNode in node.children.items():
            _search(childNode, 0, word + ch)
        return ans
                
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        groups = collections.defaultdict(Trie)
        for word in words:
            groups[len(word), word[0], word[-1]].insert(word)
            
        ans = {}
        for key in groups.keys():
            for word, changeWord in groups[key].search().items():
                ans[word] = changeWord
            
        return [ans[word] for word in words]