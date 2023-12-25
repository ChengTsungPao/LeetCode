class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        def convert(num):
            return num // n, num % n
        
        ans = [-1, -1]
        
        # get total sum
        s = 0
        for idx in range(n * n):
            curx, cury = convert(idx)
            s += grid[curx][cury]
        
        # find repeat
        idx = 0
        while idx < n * n:
            curx, cury = convert(idx)
            if grid[curx][cury] == idx + 1:
                idx += 1
                continue
            
            i, j = convert(grid[curx][cury] - 1)
            if grid[i][j] == grid[curx][cury]:
                ans[0] = grid[i][j]
                break
                
            grid[i][j], grid[curx][cury] = grid[curx][cury], grid[i][j]
            
        ans[1] = ((1 + n * n) * (n * n) // 2) - s + ans[0]
        
        return ans