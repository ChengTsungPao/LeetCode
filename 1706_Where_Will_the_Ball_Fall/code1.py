class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        
        def simulation(i, j):
            
            while i < m - 1:
                # 左牆終止
                if grid[i + 1][j] == -1 and j == 0:
                    break
                # 右牆終止
                elif grid[i + 1][j] == 1 and j == n - 1:
                    break
                # 往左邊走
                elif grid[i + 1][j] == -1 and grid[i + 1][j - 1] == -1:
                    j -= 1
                # 往右邊走
                elif grid[i + 1][j] == 1 and grid[i + 1][j + 1] == 1:
                    j += 1
                # V型終止
                else:
                    break
                    
                i += 1
                
            return j if i == m - 1 else -1
        
        
        ans = []
        
        for j in range(n):
            ans.append(simulation(-1, j))
            
        return ans