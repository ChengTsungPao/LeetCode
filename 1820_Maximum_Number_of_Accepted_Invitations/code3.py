class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        
        # Hungarian Algorithm
        
        m = len(grid)
        n = len(grid[0])
        
        matches = {}
        
        def recur(boy, visited):

            for girl in range(n):
                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)
                    
                    # 1. girl is not match => match boy and girl
                    # 2. girl is     match => try to change the previous boy's (matches[girl]) girl
                    if girl not in matches or recur(matches[girl], visited):
                        matches[girl] = boy
                        return True

            return False
                    
        for boy in range(m):
            recur(boy, set())
        
        return len(matches)