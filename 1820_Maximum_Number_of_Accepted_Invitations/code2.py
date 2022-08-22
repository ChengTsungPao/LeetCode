class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        @functools.lru_cache(None)
        def recur(boy, bitmask):
            if boy >= m:
                return 0
            
            ans = recur(boy + 1, bitmask)
            for girl in range(n):
                if grid[boy][girl] and bitmask[girl] == "0":
                    ans = max(ans, recur(boy + 1, bitmask[:girl] + "1" + bitmask[girl + 1:]) + 1)
                    
            return ans
        
        return recur(0, "0" * n)