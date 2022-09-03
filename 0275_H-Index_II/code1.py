class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        
        ans = 0
        left, right = 0, n
        
        while left <= right:
            mid = left + (right - left) // 2
            lower = n - bisect.bisect_right(citations, mid)
            upper = n - bisect.bisect_left(citations, mid)
            
            if mid < lower:
                left = mid + 1
            elif mid > upper:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
                
        return ans