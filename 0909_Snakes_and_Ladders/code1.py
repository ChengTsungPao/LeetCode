class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        
        def getElement(ID):
            ID -= 1
            row = ~(ID // n)
            col = ~(ID % n)
            if abs(row) % 2 == 1:
                col = ~col
            return board[row][col]
        

        que = collections.deque([(1, 0)])
        visited = set([1])
        
        while que:
            ID, step = que.pop()
            
            if ID == n * n:
                return step
            
            for move in range(1, 6 + 1):
                nextID = ID + move
                if not 1 <= nextID <= n * n:
                    continue
                    
                if getElement(nextID) > 0:
                    nextID = getElement(nextID)

                if nextID in visited:
                    continue
                    
                visited.add(nextID)   
                que.appendleft((nextID, step + 1))
                    
        return -1