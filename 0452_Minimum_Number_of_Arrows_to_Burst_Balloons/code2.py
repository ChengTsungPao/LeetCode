class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        ans = 0
        minEnd = -float("inf")
        
        for start, end in sorted(points):
            if start > minEnd:
                minEnd = end
                ans += 1
            else:
                minEnd = min(minEnd, end)
                
        return ans