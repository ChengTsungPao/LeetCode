class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        length = len(word)
        m = len(board)
        n = len(board[0])
        
        def rowCondition(row, start):
            ans = True
            for k in range(length):
                if board[row][start + k] != " " and board[row][start + k] != word[k]:
                    ans = False
                    break
            if ans:
                return True
            ans = True
            for k in range(length):
                if board[row][start + k] != " " and board[row][start + k] != word[~k]:
                    ans = False
                    break
            return ans    
            
        def colCondition(col, start):
            ans = True
            for k in range(length):
                if board[start + k][col] != " " and board[start + k][col] != word[k]:
                    ans = False
                    break
            if ans:
                return True
            ans = True
            for k in range(length):
                if board[start + k][col] != " " and board[start + k][col] != word[~k]:
                    ans = False
                    break
            return ans    
        
        for i in range(m):
            isEmpty = False
            start = 0
            for j in range(n):
                if board[i][j] != "#" and isEmpty == False:
                    start = j
                    isEmpty = True
                elif board[i][j] == "#" and isEmpty:
                    if j - start == length and rowCondition(i, start):
                        return True
                    isEmpty = False
            if isEmpty:
                if n - start == length and rowCondition(i, start):
                    return True   

        for j in range(n):
            isEmpty = False
            start = 0
            for i in range(m):
                if board[i][j] != "#" and isEmpty == False:
                    start = i
                    isEmpty = True
                elif board[i][j] == "#" and isEmpty:
                    if i - start == length and colCondition(j, start):
                        return True
                    isEmpty = False
            if isEmpty:
                 if m - start == length and colCondition(j, start):
                    return True     
                
        return False