class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        def isStable(i, j):
            if (i, j) in isStablePos:
                return True
            elif not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0 or (i, j) in visited:
                return False
            elif i == 0:
                return True
            visited.add((i, j))
            return isStable(i - 1, j) or isStable(i, j - 1) or isStable(i + 1, j) or isStable(i, j + 1)
        
        def markTable(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return markTable(i + 1, j) + markTable(i, j + 1) + markTable(i - 1, j) + markTable(i, j - 1) + 1
            
        # init   
        isStablePos = set()
        for i in range(m):
            for j in range(n):   
                visited = set()
                if isStable(i, j):
                    isStablePos |= visited
                else:
                    markTable(i, j)
        isStablePos = set()
                    
        # hit
        ans = []
        for i, j in hits:
            if grid[i][j] == 0:
                ans.append(0)
                continue
            
            grid[i][j] = 0
            count = 0
            
            visited = set()
            if not isStable(i + 1, j):
                count += markTable(i + 1, j)
                
            visited = set()
            if not isStable(i, j + 1):
                count += markTable(i, j + 1)
                
            visited = set()
            if not isStable(i - 1, j):
                count += markTable(i - 1, j) 
                
            visited = set()
            if not isStable(i, j - 1):
                count += markTable(i, j - 1)   
                
            ans.append(count)
            
        return ans