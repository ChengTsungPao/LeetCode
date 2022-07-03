class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        from sortedcontainers import SortedList
        
        def isOverlapping(range1, range2):
            return max(range1[0], range2[0]) < min(range1[1], range2[1])
        
        left, down = min(rectangles, key = lambda x: (x[0], x[1]))[:2]
        right, up  = max(rectangles, key = lambda x: (x[2], x[3]))[2:]
        
        n = len(rectangles)
        bst = SortedList()
            
        area = 0
        heap = []
        for i, (x1, y1, x2, y2) in enumerate(rectangles):
            area += (x2 - x1) * (y2 - y1)
            heap.append((x1,  (i + 1), y1, y2))
            heap.append((x2, -(i + 1), y1, y2))
        heapq.heapify(heap)
        
        while heap:
            x, i, y1, y2 = heapq.heappop(heap)
            if i < 0:
                bst.remove((y1, y2))
            else:
                index = bst.bisect_left((y1, y2))
                if index < len(bst) and isOverlapping((y1, y2), bst[index]):
                    return False
                if index - 1 >= 0 and isOverlapping((y1, y2), bst[index - 1]):
                    return False
                bst.add((y1, y2))
            
        return area == (right - left) * (up - down)