class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def isMineAround(x, y):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x_, y_ = x + dx, y + dy
                    if not (0 <= x_ < len(board) and 0 <= y_ < len(board[0])):
                        continue
                    count += board[x_][y_] == "M"
            return count
        
        def dfs(x, y):
            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] == "M" or board[x][y] == "B":
                return
            
            count = isMineAround(x, y)
            if count == 0:
                board[x][y] = "B"
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        x_, y_ = x + dx, y + dy
                        dfs(x_, y_)
            else:
                board[x][y] = str(count)
            
            return
        
        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            dfs(x, y)
            
        return board