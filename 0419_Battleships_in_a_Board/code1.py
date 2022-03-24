class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        m = len(board)
        n = len(board[0])
        
        def horizontal(i, j):
            while j < n and board[i][j] == "X":
                board[i][j] = "."
                j += 1
                
        def vertical(i, j):
            while i < m and board[i][j] == "X":
                board[i][j] = "."
                i += 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    horizontal(i, j + 1)
                    vertical(i + 1, j)
                    board[i][j] = "."
                    ans += 1
                    
        return ans