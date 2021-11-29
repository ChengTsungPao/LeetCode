class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        
        for r, c in points:
            row[r].add(c)
            col[c].add(r)
            
        ans = float("inf")
        for i in range(len(points)):
            r, c = points[i]
            for j in range(i + 1, len(points)):
                r_, c_ = points[j]
                if r != r_ and c != c_ and r in col[c_] and c in row[r_]:
                    ans = min(ans, abs(r - r_) * abs(c - c_))
          
        return ans if ans != float("inf") else 0