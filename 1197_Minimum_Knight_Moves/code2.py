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
            
        def startDistance(i, j):
            return ((i - x) ** 2 + (j - y) ** 2) ** 0.5
        
        def endDistance(i, j):
            return ((i - 0) ** 2 + (j - 0) ** 2) ** 0.5
            
        
        startQue = collections.deque([(0, 0, 0)])
        startFound = {(0, 0): 0}
        startMinDistance = startDistance(0, 0)
        
        endQue = collections.deque([(x, y, 0)])
        endFound = {(x, y): 0}
        endMinDistance = endDistance(x, y)
        
        while startQue or endQue:
            if startQue:
                startX, startY, startStep = startQue.pop()
                
            if endQue:
                endX, endY, endStep = endQue.pop()
            
            if (startX, startY) in endFound:
                return startStep + endFound[startX, startY]
            
            if (endX, endY) in startFound:
                return endStep + startFound[endX, endY]
            
            startMinDistance = min(startMinDistance, startDistance(startX, startY))
            endMinDistance = min(endMinDistance, endDistance(endX, endY))
            
            for index in range(8):
                startX_, startY_ = move(startX, startY, index)
                if (startX_, startY_) not in startFound and startDistance(startX_, startY_) < startMinDistance + 10:
                    startQue.appendleft((startX_, startY_, startStep + 1))
                    startFound[startX_, startY_] = startStep + 1
                
                endX_, endY_ = move(endX, endY, index)
                if (endX_, endY_) not in startFound and endDistance(endX_, endY_) < endMinDistance + 10:
                    endQue.appendleft((endX_, endY_, endStep + 1))
                    endFound[endX_, endY_] = endStep + 1    
                    
        return -1