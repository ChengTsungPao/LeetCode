class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        row = collections.defaultdict(int)
        col = collections.defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                row[i] = max(row[i], grid[i][j])
                col[j] = max(col[j], grid[i][j])
                
        ans = 0
        for i in range(m):
            for j in range(n):
                height = min(row[i], col[j])
                if height > grid[i][j]:
                    ans += height - grid[i][j]
                    
        return ans