class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        def condition(length):
            count = 0
            for r in ribbons:
                count += r // length
            return count >= k
        
        
        left = 1
        right = max(ribbons) + 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
                
        return left - 1