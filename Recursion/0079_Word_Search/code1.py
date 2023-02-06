class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        w_len = len(word)
        
        def recur(i, j, k): # board[i][j], word[k]
            if k >= w_len:
                return True
            elif not (0 <= i < m and 0 <= j < n) or board[i][j] != word[k]:
                return False
            
            # backtracking
            ch = board[i][j]
            board[i][j] = ""
            
            # searching
            ret = False
            ret = ret or recur(i + 1, j, k + 1)
            ret = ret or recur(i, j + 1, k + 1)
            ret = ret or recur(i - 1, j, k + 1)
            ret = ret or recur(i, j - 1, k + 1)
            
            # backtracking
            board[i][j] = ch
            return ret
        
        for i in range(m):
            for j in range(n):
                if recur(i, j, 0):
                    return True
                
        return False