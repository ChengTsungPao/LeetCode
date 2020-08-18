class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = collections.defaultdict(set)
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] in row or board[j][i] in col or board[i][j] in square[i // 3, j // 3]:
                    return False
                if board[i][j] != ".":
                    row.add(board[i][j])
                    square[i // 3, j // 3].add(board[i][j])
                if board[j][i] != ".":
                    col.add(board[j][i])
        return True