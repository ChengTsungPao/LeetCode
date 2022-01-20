class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        def move(i, j, index):
            if index == 0:
                return i - 1, j - 2
            elif index == 1:
                return i + 1, j - 2            
            elif index == 2:
                return i - 1, j + 2                
            elif index == 3:
                return i + 1, j + 2   
            elif index == 4:
                return i - 2, j - 1
            elif index == 5:
                return i + 2, j - 1            
            elif index == 6:
                return i - 2, j + 1                
            elif index == 7:
                return i + 2, j + 1 
            else:
                return i, j
            
        def distance(i, j):
            return ((i - x) ** 2 + (j - y) ** 2) ** 0.5
            
            
        que = collections.deque([(0, 0, 0)])
        found = set([(0, 0)])
        minDistance = distance(0, 0)
        
        while que:
            i, j, step = que.pop()
            minDistance = min(minDistance, distance(i, j))
            
            if i == x and j == y:
                return step
            
            for index in range(8):
                i_, j_ = move(i, j, index)
                
                if (i_, j_) in found or distance(i_, j_) >= minDistance + 10:
                    continue
                
                que.appendleft((i_, j_, step + 1))
                found.add((i_, j_))
                
        return -1
    