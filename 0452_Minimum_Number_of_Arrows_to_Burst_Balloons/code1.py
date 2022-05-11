class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        record = []
        for i, (start, end) in enumerate(points):
            record.append((start, -(i + 1)))
            record.append((end, i + 1))
        
        ans = 0
        remove = set()
        current = set()
        
        for time, target in sorted(record):
            if target in remove:
                continue
            
            if target > 0:
                ans += 1
                remove |= current
                current = set()

            current.add(-target)
            
        return ans