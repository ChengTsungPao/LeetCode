class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        # dp => matrix[i][j]的意義為(i, j)是正方形的右下角有幾種可能
        
        ans = matrix[0][0]
        
        for i in range(1, len(matrix)):
            ans += matrix[i][0]
            
        for j in range(1, len(matrix[0])):
            ans += matrix[0][j]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                ans += matrix[i][j]
                
        return ans