class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        n = len(board[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or board[i][j] == "X" or board[i][j] == "OK":
                return
            
            board[i][j] = "OK"
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "OK":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"