class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        status = set()
        
        def check(i, j):
            if (i, j) not in status:
                status.add((i, j))
            else:
                status.remove((i, j))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    check(i + 0.5, j)
                    check(i - 0.5, j)
                    check(i, j + 0.5)
                    check(i, j - 0.5)

        return len(status)