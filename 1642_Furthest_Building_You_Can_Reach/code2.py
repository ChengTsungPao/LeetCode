class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        
        def condition(reachIndex):
            hArr = []
            for i in range(1, reachIndex + 1):
                if heights[i] - heights[i - 1] > 0:
                    hArr.append(heights[i] - heights[i - 1])
            
            hArr.sort()
            _sum = sum(hArr[:-ladders]) if ladders > 0 else sum(hArr)
            return _sum <= bricks
        
        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
                
        return left - 1