class Trie:
    def __init__(self, board):
        self.children = {"countWord": 0, "isWord": False}
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        
    def insert(self, word):
        # insert word
        node = self.children
        for ch in word:
            if ch not in node:
                node[ch] = {"countWord": 0, "isWord": False}
            node = node[ch]
        isInsertBefore = node["isWord"]
        node["isWord"] = True
        node["word"] = word
        
        # cal how many word in children
        if not isInsertBefore:
            node = self.children
            for ch in word:
                node["countWord"] += 1
                node = node[ch]
            node["countWord"] += 1
                
    def search(self):
        
        # start searching at (i, j)
        def _search(i, j, node):
            if not (0 <= i < self.m and 0 <= j < self.n):
                return set()
            
            ch = self.board[i][j]
            if ch not in node:
                return set()
            
            # backtracking
            self.board[i][j] = ""
            
            child = node[ch]
            wordSet = {child["word"]} if child["isWord"] else set()
            for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                wordSet |= _search(i_, j_, child)
                # pruing: if all children words are in wordSet, then stop backtracking
                if len(wordSet) == node["countWord"]: break
            
            # backtracking
            self.board[i][j] = ch
            return wordSet
        
        # get answer
        wordSet = set()
        for i in range(self.m):
            for j in range(self.n):
                wordSet |= _search(i, j, self.children)
                
        return list(wordSet)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie(board)
        for word in words:
            trie.insert(word)

        return trie.search()