class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            
            if (not (0 <= i < len(grid) and 0 <= j < len(grid[0]))) or grid[i][j] == 0 or grid[i][j] == number:
                return 0
            
            grid[i][j] = number
            
            return dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1) + 1
        
        
        number = -1
        count = {0: 0}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count[number] = dfs(i, j)
                    number -= 1

                    
        ans = 1
        noZero = True
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = 1
                
                if grid[i][j] == 0:
                    kind = set()
                    for row, col in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                            continue
                        kind.add(grid[row][col])
   
                    for number in kind:
                        temp += count[number]
                        
                    noZero = False
                    
                ans = max(ans, temp)      

        return len(grid) * len(grid[0]) if noZero else ans
