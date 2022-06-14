class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        minXDifference = 0 if x1 <= xCenter <= x2 else min(abs(xCenter - x1), abs(xCenter - x2))
        minYDifference = 0 if y1 <= yCenter <= y2 else min(abs(yCenter - y1), abs(yCenter - y2))
        
        return minXDifference ** 2 + minYDifference ** 2 <= radius ** 2