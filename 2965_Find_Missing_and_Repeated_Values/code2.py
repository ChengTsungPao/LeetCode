class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        def convert(num):
            return num // n, num % n
        
        idx = 0
        while idx < n * n:
            curx, cury = convert(idx)
            if grid[curx][cury] == idx + 1:
                idx += 1
                continue
            
            i, j = convert(grid[curx][cury] - 1)
            if grid[i][j] == grid[curx][cury]:
                idx += 1
                continue
                
            grid[i][j], grid[curx][cury] = grid[curx][cury], grid[i][j]

        for idx in range(n * n):
            curx, cury = convert(idx)
            if grid[curx][cury] != idx + 1:
                return [grid[curx][cury], idx + 1]
                
        return [-1, -1]