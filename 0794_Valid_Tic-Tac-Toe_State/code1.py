class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        n = 3
        winnerLine = collections.defaultdict(list)
        
        def countLine(_str, indices):
            if _str == "XXX":
                winnerLine["X"].append(indices.copy())
            elif _str == "OOO":
                winnerLine["O"].append(indices.copy())
        
        # countWinner row
        for i in range(n):
            _str = ""
            indices = set()
            for j in range(n):
                _str += board[i][j]
                indices.add((i, j))
            countLine(_str, indices)
        
        # countWinner col
        for j in range(n):
            _str = ""
            indices = set()
            for i in range(n):
                _str += board[i][j]
                indices.add((i, j))
            countLine(_str, indices)
        
        # countWinner incline
        _str1, indices1 = "", set()
        _str2, indices2 = "", set()
        for i in range(n):
            _str1 += board[i][i]
            _str2 += board[i][~i]
            indices1.add((i, i))
            indices2.add((i, n + (~i)))
        countLine(_str1, indices1)
        countLine(_str2, indices2)
        
        # count "X" and "O"
        countKind = collections.Counter("".join(board))
        
        
        X_WinnerLineCount = len(winnerLine["X"])
        O_WinnerLineCount = len(winnerLine["O"])
        X_O_differenceCount = countKind["X"] - countKind["O"]
        
        if not (0 <= X_O_differenceCount <= 1):
            return False
        elif X_O_differenceCount == 0 and X_WinnerLineCount > 0:
            return False
        elif X_O_differenceCount == 1 and O_WinnerLineCount > 0:
            return False
        
        if X_WinnerLineCount > 2 or O_WinnerLineCount > 2 or (X_WinnerLineCount > 0 and O_WinnerLineCount > 0):
            return False
        elif X_WinnerLineCount == 2 and len(winnerLine["X"][0] & winnerLine["X"][1]) == 0:
            return False
        elif O_WinnerLineCount == 2 and len(winnerLine["O"][0] & winnerLine["O"][1]) == 0:
            return False
            
        return True