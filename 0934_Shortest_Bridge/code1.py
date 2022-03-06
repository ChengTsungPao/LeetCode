class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        stack = []
        que = collections.deque()
        
        isFind = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    grid[i][j] = 2
                    isFind = True
                    break
            if isFind:
                break
      
        while stack:
            i, j = stack.pop()
            
            for i_, j_ in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_] == 2:
                    continue
                    
                if grid[i_][j_] == 0:
                    grid[i_][j_] = 2
                    que.appendleft((i_, j_, 1)) 
                    continue
                    
                grid[i_][j_] = 2
                stack.append((i_, j_))

        while que:
            i, j, step = que.pop()
            
            for i_, j_ in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_] == 2:
                    continue

                if grid[i_][j_] == 1:
                    return step
                
                grid[i_][j_] = 2
                que.appendleft((i_, j_, step + 1))

        return -1