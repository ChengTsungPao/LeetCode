class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def recur(i, j, index):
            
            if index == len(word):
                return True
            
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != word[index]:
                return False
            
            ch = board[i][j]
            board[i][j] = "#"
            
            ret = recur(i + 1, j + 0, index + 1) or \
                  recur(i + 0, j + 1, index + 1) or \
                  recur(i - 1, j + 0, index + 1) or \
                  recur(i + 0, j - 1, index + 1)
            
            board[i][j] = ch
            
            return ret
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if recur(i, j, 0):
                    return True
                
        return False