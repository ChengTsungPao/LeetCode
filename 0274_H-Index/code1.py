class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        
        ans = 0
        left, right = 0, 5000
        
        while left <= right:
            mid = left + (right - left) // 2
            lower = len(citations) - bisect.bisect_right(citations, mid)
            upper = len(citations) - bisect.bisect_left(citations, mid)

            if lower > mid:
                left = mid + 1
            elif upper < mid:
                right = mid - 1
            else:
                ans = max(ans, mid)
                left = mid + 1   

        return ans