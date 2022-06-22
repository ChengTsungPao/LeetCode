class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        n = len(rectangles)
        
        left, down = min(rectangles, key = lambda x: (x[0], x[1]))[:2]
        right, up  = max(rectangles, key = lambda x: (x[2], x[3]))[2:]
        
        def isOverlapping(rectangle1, rectangle2):
            left1, down1, right1, up1 = rectangle1
            left2, down2, right2, up2 = rectangle2
            return right1 > left2 and left1 < right2 and up1 > down2 and down1 < up2
        
        for d in range(4):        
            rectangles = sorted(rectangles, key = lambda x: x[d])
            for i in range(n - 1):
                if isOverlapping(rectangles[i], rectangles[i + 1]):
                    return False
            
        area = 0
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            
        return area == (right - left) * (up - down)