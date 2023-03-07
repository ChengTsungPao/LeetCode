class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def condition(curtime):
            return sum([curtime // t for t in time]) >= totalTrips
        
        ans = -1
        left = 0
        right = totalTrips * min(time)
        while left <= right:
            mid = left + (right - left) // 2
            if condition(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans