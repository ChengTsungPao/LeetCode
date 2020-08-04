class WordDictionary(TreeNode):
    def __init__(self):
        self.trie = collections.defaultdict(dict)    

    def addWord(self, word: str) -> None:
        pointer = self.trie
        for ch in word:
            if ch not in pointer:
                pointer[ch] = {}
            pointer = pointer[ch]   
        pointer["bool"] = True
        
    def search(self, word: str) -> bool:
        def dfs(node, index):
            nonlocal word
            if index == len(word):
                return "bool" in node
            if word[index] == ".":
                for ch in node:
                    if ch != "bool" and dfs(node[ch], index + 1):
                        return True
            elif word[index] in node:
                if dfs(node[word[index]], index + 1):
                    return True
                
        if(dfs(self.trie, 0)):
            return True
        else:
            return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)