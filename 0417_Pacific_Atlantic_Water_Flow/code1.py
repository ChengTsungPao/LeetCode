class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(i, j, h = 0):
            if not (0 <= i < m and 0 <= j < n) or (i, j) in found or h > heights[i][j]:
                return
            
            count[i][j] += 1
            found.add((i, j))
            
            dfs(i + 1, j + 0, heights[i][j])
            dfs(i + 0, j + 1, heights[i][j])
            dfs(i - 1, j + 0, heights[i][j])
            dfs(i + 0, j - 1, heights[i][j])

            
        m, n = len(heights), len(heights[0])
        count = [[0] * n for _ in range(m)]
        
        found = set()
        for i in range(m):
            dfs(i, 0)

        for j in range(n):
            dfs(0, j)

        found = set()
        for i in range(m):
            dfs(i, n - 1)

        for j in range(n):
            dfs(m - 1, j)
            
        ans = []
        for i in range(m):
            for j in range(n):
                if count[i][j] == 2:
                    ans.append((i, j))
                    
        return ans
