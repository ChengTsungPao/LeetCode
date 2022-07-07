class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        length = len(hits)
        
        EMPTY = 0
        UNSTABLE = 1
        STABLE = 2

        def dfs(x, y, state):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == EMPTY or grid[x][y] == state:
                return 0
            grid[x][y] = state
            return dfs(x + 1, y, state) + dfs(x, y + 1, state) + dfs(x - 1, y, state) + dfs(x, y - 1, state) + 1

        ans = [0] * length
        for i, (x, y) in enumerate(hits):
            if grid[x][y] == EMPTY:
                ans[i] = -1
            else:
                grid[x][y] = EMPTY

        for y in range(n):
            if grid[0][y] == UNSTABLE:
                dfs(0, y, STABLE)

        for i in range(length - 1, -1, -1):
            if ans[i] < 0:
                ans[i] = 0
                continue
            
            x, y = hits[i]
            isStable = (x == 0)
            for x_, y_ in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if (0 <= x_ < m and 0 <= y_ < n) and grid[x_][y_] == STABLE:
                    isStable = True
                    break
            
            grid[x][y] = UNSTABLE
            if isStable:
                ans[i] = dfs(x, y, STABLE) - 1

        return ans