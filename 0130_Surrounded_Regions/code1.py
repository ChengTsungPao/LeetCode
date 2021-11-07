class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(i, j, ch):

            if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return True
            
            if board[i][j] == "X" or board[i][j] == ch:
                return False
            
            board[i][j] = ch
            isVisited.add((i, j))
            
            ret = False
            ret = dfs(i + 1, j + 0, ch) or ret
            ret = dfs(i - 1, j + 0, ch) or ret
            ret = dfs(i + 0, j + 1, ch) or ret
            ret = dfs(i + 0, j - 1, ch) or ret
            
            return ret

        isVisited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in isVisited and board[i][j] == "O" and dfs(i, j, "V") == False:
                    dfs(i, j, "X")
                else:
                    dfs(i, j, "O")