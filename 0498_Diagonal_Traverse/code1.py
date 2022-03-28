class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])
        
        ans = []
        direction = True
        
        for index in range(m):
            layer = []
            
            i, j = index, 0
            while i >= 0 and j < n:
                layer.append(mat[i][j])
                i -= 1
                j += 1
                
            if direction:
                ans += layer
            else:
                ans += layer[::-1]
                
            direction = not direction
                    
        for index in range(1, n):
            layer = []
            
            i, j = m - 1, index
            while i >= 0 and j < n:
                layer.append(mat[i][j])
                i -= 1
                j += 1
                    
            if direction:
                ans += layer
            else:
                ans += layer[::-1]
                
            direction = not direction
                
        return ans