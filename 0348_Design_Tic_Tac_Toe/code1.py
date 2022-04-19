class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [[0] * n, [0] * n]
        self.col = [[0] * n, [0] * n]
        self.dia = [[0] * 2, [0] * 2]
        
    def updateRowCol(self, row, col, player):
        self.row[player - 1][row] += 1
        self.col[player - 1][col] += 1
        return self.row[player - 1][row] == self.n or self.col[player - 1][col] == self.n
        
    def updateDiagonal(self, row, col, player):
        if row == col:
            self.dia[player - 1][0] += 1
        if -(0 - row) == (self.n - 1 - col):
            self.dia[player - 1][1] += 1
        return self.dia[player - 1][0] == self.n or self.dia[player - 1][1] == self.n
        
    def move(self, row: int, col: int, player: int) -> int:
        if self.updateRowCol(row, col, player) or self.updateDiagonal(row, col, player):
            return player
        else:
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)