class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def getLine(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            m = (y1 - y2) / (x1 - x2) if x1 != x2 else float("inf")
            c = y1 - m * x1  if x1 != x2 else x1
            return round(m, 8), round(c, 8)
        
        def solve(n):
            # x(x - 1) = 2n => (1 + (1 + 8n) ** 0.5) / 2
            return int(1 + (1 + 8 * n) ** 0.5) // 2
        
        n = len(points)
        status = collections.defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                m, c = getLine(points[i], points[j])
                status[m, c] += 1

        return solve(max(status.values(), default = 0))