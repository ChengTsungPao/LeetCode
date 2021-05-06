class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        def bfs(i, j):
            que = collections.deque()
            que.appendleft((i, j))
            grid[i][j] = "0"
            while que:
                i, j = que.pop()
                if i > 0 and grid[i - 1][j] == "1":
                    que.appendleft((i - 1, j))
                    grid[i - 1][j] = "0"
                if i < height - 1 and grid[i + 1][j] == "1":
                    que.appendleft((i + 1, j))
                    grid[i + 1][j] = "0"
                if j < width - 1 and grid[i][j + 1] == "1":
                    que.appendleft((i, j + 1))
                    grid[i][j + 1] = "0"
                if j > 0 and grid[i][j - 1] == "1":
                    que.appendleft((i, j - 1))
                    grid[i][j - 1] = "0"
                
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans