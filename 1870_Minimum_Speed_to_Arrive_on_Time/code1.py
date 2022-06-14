class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        n = len(dist)
        
        def condition(speed):
            time = 0
            for i in range(n - 1):
                time += math.ceil(dist[i] / speed)
            time += dist[-1] / speed
            return time <= hour
        
        
        left = 1
        right = 10 ** 7 + 1
        while left < right:
            mid = left + (right - left) // 2
            if not condition(mid):
                left = mid + 1
            else:
                right = mid
                
        return left if left < 10 ** 7 + 1 else -1