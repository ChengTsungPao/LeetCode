class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return
            
            grid[i][j] = 2
            
            dfs(i + 1, j + 0)
            dfs(i + 0, j + 1)
            dfs(i - 1, j + 0)
            dfs(i + 0, j - 1)
            
        
        que = collections.deque()
        
        isVisited = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if isVisited:
                        que.appendleft((i, j, 0))
                    else:
                        dfs(i, j)
                        isVisited = True
                        
        while que:
            i, j, step = que.pop()
            
            for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_] == 1:
                    continue
                    
                if grid[i_][j_] == 2:
                    return step
                
                grid[i_][j_] = 1
                que.appendleft((i_, j_, step + 1))
                
        return -1