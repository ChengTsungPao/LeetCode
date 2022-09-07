class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        n = len(intervals)
        
        ans = []
        sorted_intervals = sorted([(start, j) for j, (start, end) in enumerate(intervals)])
        
        for i, (start, end) in enumerate(intervals):            
            j = bisect.bisect_left(sorted_intervals, (end, 0))
            if j >= n:
                ans.append(-1)
            else:
                ans.append(sorted_intervals[j][1])
            
        return ans