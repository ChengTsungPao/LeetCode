class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def recur(boy, visited):
            if boy >= m:
                return 0
            
            ans = recur(boy + 1, visited)
            for girl in range(n):
                if grid[boy][girl] and girl not in visited:
                    ans = max(ans, recur(boy + 1, visited | {girl}) + 1)
                    
            return ans
        
        return recur(0, set())