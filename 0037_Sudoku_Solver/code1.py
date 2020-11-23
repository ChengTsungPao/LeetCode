class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        status = []
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    status.append((i, j))
                else:
                    row[i].add(int(board[i][j]))
                    col[j].add(int(board[i][j]))
                    square[i // 3, j // 3].add(int(board[i][j]))        

        def backtracking(row, col, square, status):
            if len(status) == 0:
                return True
            
            i, j = status.pop()
            
            for n in range(1, 10):
                if n not in row[i] and n not in col[j] and n not in square[i // 3, j // 3]:
                    row[i].add(n)
                    col[j].add(n)
                    square[i // 3, j // 3].add(n)
                    board[i][j] = str(n)
                    if backtracking(row, col, square, status):
                        return True
                    row[i].remove(n)
                    col[j].remove(n)
                    square[i // 3, j // 3].remove(n)
                    board[i][j] = "."
                    
            status.append((i, j))

        backtracking(row, col, square, status)       