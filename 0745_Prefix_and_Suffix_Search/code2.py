class WordFilter:

    def __init__(self, words: List[str]):
        self.trie_list = {}
        self.trie_set  = {}
        self.build(words)
        
    def build(self, words):
        wordSet = set()
        for index in range(len(words) - 1, -1, -1):
            word = words[index]
            if word not in wordSet:
                self.insert(word, index)
                wordSet.add(word)
        
    def insert(self, word, index):
        node = self.trie_list
        for ch in word:
            if ch not in node:
                node[ch] = {"indexList": []}
            node = node[ch]
            node["indexList"].append(index)
            
        node = self.trie_set
        for ch in word[::-1]:
            if ch not in node:
                node[ch] = {"indexSet": set()}
            node = node[ch]
            node["indexSet"].add(index)
            
    def search(self, pref, suff):
        isEmpty = False
        node = self.trie_list
        for ch in pref:
            if ch not in node:
                isEmpty = True
                break
            node = node[ch]
        indexList = node["indexList"] if not isEmpty else []
        
        isEmpty = False
        node = self.trie_set
        for ch in suff[::-1]:
            if ch not in node:
                isEmpty = True
                break
            node = node[ch]
        indexSet = node["indexSet"] if not isEmpty else set()
        
        return indexList, indexSet

    def f(self, pref: str, suff: str) -> int:
        indexList, indexSet = self.search(pref, suff)
        for index in indexList:
            if index in indexSet:
                return index
        return -1
        
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)