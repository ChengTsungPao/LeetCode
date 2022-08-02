class WordFilter:

    def __init__(self, words: List[str]):
        self.trie_list = {}
        self.trie_set  = {}
        self.index = {}
        self.build(words)
        
    def build(self, words):
        for word in words[::-1]:
            self.insert(word)
            
        for i, word in enumerate(words):
            self.index[word] = i
        
    def insert(self, word):
        node = self.trie_list
        for ch in word:
            if ch not in node:
                node[ch] = {"wordList": []}
            node = node[ch]
            node["wordList"].append(word)
            
        node = self.trie_set
        for ch in word[::-1]:
            if ch not in node:
                node[ch] = {"wordSet": set()}
            node = node[ch]
            node["wordSet"].add(word)
            
    def search(self, pref, suff):
        isEmpty = False
        node = self.trie_list
        for ch in pref:
            if ch not in node:
                isEmpty = True
                break
            node = node[ch]
        wordList = node["wordList"] if not isEmpty else []
        
        isEmpty = False
        node = self.trie_set
        for ch in suff[::-1]:
            if ch not in node:
                isEmpty = True
                break
            node = node[ch]
        wordSet = node["wordSet"] if not isEmpty else set()
        
        return wordList, wordSet

    def f(self, pref: str, suff: str) -> int:
        wordList, wordSet = self.search(pref, suff)
        for word in wordList:
            if word in wordSet:
                return self.index[word]
        return -1
        
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)