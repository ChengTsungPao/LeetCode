class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def bfs(i, j):            
            que = collections.deque([(i, j)])
            grid[i][j] == "0"
            
            while que:
                i, j = que.popleft()
                
                for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_] == "0":
                        continue
                        
                    que.append((i_, j_))
                    grid[i_][j_] = "0"

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
                
        return ans