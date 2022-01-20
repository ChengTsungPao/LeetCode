class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = self.setup(matrix)
        
    def setup(self, matrix):
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            matrix[i][0] += matrix[i - 1][0]
            
        for j in range(1, n):
            matrix[0][j] += matrix[0][j - 1]
            
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
                       
        return matrix
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1 - 1]
        elif col1 == 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        else:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 - 1] + self.dp[row1 - 1][col1 - 1]

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        obj = NumMatrix(mat)
        m, n = len(mat), len(mat[0])
        
        def findInclineMaxlength(i, j):
            maxlength = 0
            i_, j_ = i, j
            while i_ < m and j_ < n:
                if obj.sumRegion(i, j, i_, j_) <= threshold:
                    maxlength = max(maxlength, i_ - i + 1)
                    i_, j_ = i_ + 1, j_ + 1
                else:
                    i, j = i + 1, j + 1
                    if i > i_: i_, j_ = i_ + 1, j_ + 1
            return maxlength
        
        
        ans = findInclineMaxlength(0, 0)
        
        for i in range(1, m):
            ans = max(ans, findInclineMaxlength(i, 0))
            
        for j in range(1, n):
            ans = max(ans, findInclineMaxlength(0, j))
        
        return ans