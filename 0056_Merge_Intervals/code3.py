class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        intervals.sort()
        
        ans = []
        starti, endi = intervals[0]
        for j in range(n):
            startj, endj = intervals[j]
            if endi < startj:
                ans.append([starti, endi])
                starti, endi = startj, endj
            else:
                starti, endi = min(starti, startj), max(endi, endj)
        ans.append([starti, endi])
        
        return ans