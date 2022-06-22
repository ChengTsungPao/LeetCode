class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            corners ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
            area += (x2 - x1) * (y2 - y1)

        if len(corners) != 4:
            return False
                        
        (left, down), (right, up) = min(corners), max(corners)
        
        return area == (right - left) * (up - down)