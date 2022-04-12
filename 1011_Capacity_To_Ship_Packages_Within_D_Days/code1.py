class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def condition(maxWeight):
            time = 1
            capacity = 0
            
            for w in weights:
                if capacity + w > maxWeight:
                    time += 1
                    capacity = 0
                capacity += w
                
                if time > days:
                    return False
                
            return True
        
        
        left = ans = max(weights)
        right = sum(weights)
        
        while left <= right:
            mid = left + (right - left) // 2
            if condition(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans