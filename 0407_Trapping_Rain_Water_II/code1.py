class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m = len(heightMap)
        n = len(heightMap[0])
        
        def dfs(i, j, height):
            nonlocal bound
            
            if not (0 <= i < m and 0 <= j < n):
                return False
            
            if height < heightMap[i][j]:
                bound = min(bound, heightMap[i][j])
                return True
            
            if (i, j) in visited:
                return True
            
            visited.add((i, j))
            
            ret = True
            ret = ret and dfs(i + 0, j + 1, height)
            ret = ret and dfs(i + 1, j + 0, height)
            ret = ret and dfs(i + 0, j - 1, height)
            ret = ret and dfs(i - 1, j + 0, height)
            
            return ret
        
        ans = 0
        for i in range(m):
            for j in range(n):
                bound = float("inf")
                visited = set()
                if dfs(i, j, heightMap[i][j]):
                    for x, y in visited:
                        ans += bound - heightMap[x][y]
                        heightMap[x][y] = bound
                        
        return ans