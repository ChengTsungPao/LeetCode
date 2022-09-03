class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        def get_1D_overlapping_length(a1, a2, b1, b2):
            c1 = max(a1, b1)
            c2 = min(a2, b2)
            return c2 - c1 if c2 > c1 else 0
        
        def getRectangleArea(x1, y1, x2, y2):
            return (x2 - x1) * (y2 - y1)
        
        h = get_1D_overlapping_length(ax1, ax2, bx1, bx2)
        w = get_1D_overlapping_length(ay1, ay2, by1, by2)
        
        area1 = getRectangleArea(ax1, ay1, ax2, ay2)
        area2 = getRectangleArea(bx1, by1, bx2, by2)
        
        return area1 + area2 - h * w