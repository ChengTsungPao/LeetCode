class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            grid[x][y] = "-1"
            if(x+1<len(grid)):
                if(grid[x+1][y]=="1"):
                    dfs(x+1,y)
            if(y+1<len(grid[0])):
                if(grid[x][y+1]=="1"):
                    dfs(x,y+1)
            if(x-1>=0):
                if(grid[x-1][y]=="1"):
                    dfs(x-1,y)
            if(y-1>=0):
                if(grid[x][y-1]=="1"):
                    dfs(x,y-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    dfs(i,j)
                    count += 1
        return count