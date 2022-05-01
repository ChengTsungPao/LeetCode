class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def condition(k):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / k)
            return hour <= h
        
        
        left = 1
        right = max(piles) + 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if not condition(mid):
                left = mid + 1
            else:
                right = mid
                
        return left