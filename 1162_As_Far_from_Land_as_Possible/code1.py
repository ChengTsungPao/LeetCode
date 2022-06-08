class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    stack.append((i, j))
        
        level = -1
        while stack:
            
            newStack = []
            while stack:
                i, j = stack.pop()
                
                for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_]:
                        continue
                    
                    grid[i_][j_] = 1
                    newStack.append((i_, j_))
            
            stack = newStack
            level += 1
            
        return level if level > 0 else -1