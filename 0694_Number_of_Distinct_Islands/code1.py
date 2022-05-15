class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return None
            
            visited.append((i, j))
            grid[i][j] = 0
            
            dfs(i + 0, j + 1)
            dfs(i + 1, j + 0)
            dfs(i - 1, j + 0)
            dfs(i + 0, j - 1)
            
        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = []
                    dfs(i, j)
                    
                    islandKey = ""
                    visited.sort()
                    shiftX, shiftY = visited[0]
                    for x, y in visited:
                        islandKey += "{}_{}_".format(x - shiftX, y - shiftY)
                    ans.add(islandKey)
                    
        return len(ans)