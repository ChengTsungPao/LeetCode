class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        length = len(hits)

        def dfs(x, y, target):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 0 or grid[x][y] == target:
                return 0
            grid[x][y] = target
            return dfs(x + 1, y, target) + dfs(x, y + 1, target) + dfs(x - 1, y, target) + dfs(x, y - 1, target) + 1

        ans = [0] * length
        for i, (x, y) in enumerate(hits):
            if grid[x][y] == 0:
                ans[i] = -1
            else:
                grid[x][y] = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    grid[x][y] = 2

        for y in range(n):
            if grid[0][y] == 2:
                dfs(0, y, 1)

        for i in range(length - 1, -1, -1):
            if ans[i] < 0:
                ans[i] = 0
                continue
            
            x, y = hits[i]
            isStable = (x == 0)
            for x_, y_ in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if (0 <= x_ < m and 0 <= y_ < n) and grid[x_][y_] == 1:
                    isStable = True
                    break
            
            grid[x][y] = 2
            if isStable:
                ans[i] = dfs(x, y, 1) - 1

        return ans