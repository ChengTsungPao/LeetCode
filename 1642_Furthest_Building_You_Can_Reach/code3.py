class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        
        ans = 0
        heap = []
        bricksCost = 0
        
        for i in range(1, n):
            h = heights[i] - heights[i - 1]
            if h > 0: 
                heapq.heappush(heap, h)
                
            if len(heap) > ladders:
                bricksCost += heapq.heappop(heap)
                
            if bricksCost <= bricks:
                ans = i
            else:
                break
                
        return ans