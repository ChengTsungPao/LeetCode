class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        def check(i, j):
            target = board[i][j]
            vertical = set([(i, j)])
            horizontal = set([(i, j)])
            
            index = i
            while index < len(board) and board[index][j] == target:
                vertical.add((index, j))
                index += 1
            index = i    
            while index >= 0 and board[index][j] == target:
                vertical.add((index, j))
                index -= 1
            
            index = j
            while index < len(board[0]) and board[i][index] == target:
                horizontal.add((i, index))
                index += 1
            index = j    
            while index >= 0 and board[i][index] == target:
                horizontal.add((i, index))
                index -= 1
                
            if len(vertical) < 3:
                vertical = set()
            if len(horizontal) < 3:
                horizontal = set()    
            return vertical | horizontal
        
        
        def findCrush():
            isEmpty = set()            
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != 0 and (i, j) not in isEmpty:
                        isEmpty |= check(i, j)
                        
            for x, y in isEmpty:
                board[x][y] = 0
            return len(isEmpty) > 0
        
        
        def crushing():
            for j in range(len(board[0])):
                colArr = []
                for i in range(len(board) - 1, -1, -1):
                    if board[i][j] != 0:
                        colArr.append(board[i][j])
                
                for i in range(len(board) - 1, -1, -1):
                    if len(board) - i - 1 < len(colArr):
                        board[i][j] = colArr[len(board) - i - 1]
                    else:
                        board[i][j] = 0

                        
        while findCrush():
            crushing()
            
        return board