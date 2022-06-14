class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        def distance(x1, y1, x2, y2):
            return (x1 - x2) ** 2 + (y1 - y2) ** 2
        
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True
        
        if x1 <= xCenter <= x2:
            return abs(yCenter - y1) <= radius or abs(yCenter - y2) <= radius
        
        if y1 <= yCenter <= y2:
            return abs(xCenter - x1) <= radius or abs(xCenter - x2) <= radius
        
        return distance(xCenter, yCenter, x1, y1) <= radius ** 2 or \
               distance(xCenter, yCenter, x1, y2) <= radius ** 2 or \
               distance(xCenter, yCenter, x2, y1) <= radius ** 2 or \
               distance(xCenter, yCenter, x2, y2) <= radius ** 2