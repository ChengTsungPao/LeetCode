class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        def findZeroPosition(board):
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0:
                        return i, j
            return -1, -1
        
        que = collections.deque([[board, 0]])
        cache = set([str(board)])
        
        while que:
            board, step = que.popleft()
            
            if board == [[1, 2, 3], [4, 5, 0]]:
                return step
            
            i, j = findZeroPosition(board)
            for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if not (0 <= i_ < 2 and 0 <= j_ < 3):
                    continue
                    
                nextBoard = copy.deepcopy(board)
                nextBoard[i][j], nextBoard[i_][j_] = nextBoard[i_][j_], nextBoard[i][j]
                
                key = str(nextBoard)
                if key in cache:
                    continue
                    
                que.append([nextBoard, step + 1])
                cache.add(key)
                
        return -1