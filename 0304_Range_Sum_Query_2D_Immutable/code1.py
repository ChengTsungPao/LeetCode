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
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)