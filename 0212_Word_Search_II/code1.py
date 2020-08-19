class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        pointer = self.root
        for ch in word:
            if ch not in pointer:
                pointer[ch] = {}
            pointer = pointer[ch]   
        pointer["bool"] = True
        
    def search(self, word: str) -> bool:
        pointer = self.root
        for ch in word:
            if ch not in pointer:
                return False
            pointer = pointer[ch]
        return "bool" in pointer      
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(i, j, trie, str_, path):
            nonlocal ans
            if "bool" in trie:
                ans.add(str_)
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or (i, j) in path or board[i][j] not in trie :
                return None
            dfs(i + 1, j, trie[board[i][j]], str_ + board[i][j], path | set([(i, j)]))
            dfs(i - 1, j, trie[board[i][j]], str_ + board[i][j], path | set([(i, j)]))
            dfs(i, j + 1, trie[board[i][j]], str_ + board[i][j], path | set([(i, j)]))
            dfs(i, j - 1, trie[board[i][j]], str_ + board[i][j], path | set([(i, j)]))
            
        trie = Trie()
        for word in words:
            trie.insert(word) 

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root, "", set())

        return list(ans)