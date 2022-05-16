class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0
        minEnd = -float("inf")
        
        for start, end in sorted(intervals):
            if start >= minEnd:
                minEnd = end
            else:
                minEnd = min(minEnd, end)
                count += 1
                
        return count