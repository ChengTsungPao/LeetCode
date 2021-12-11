class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        maxLength = 0
        
        for i in range(len(matrix)):
            matrix[i][0] = int(matrix[i][0])
            maxLength = max(maxLength, matrix[i][0])
        
        for j in range(len(matrix[0])):
            matrix[0][j] = int(matrix[0][j])
            maxLength = max(maxLength, matrix[0][j])
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                
                matrix[i][j] = int(matrix[i][j])
                
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

                maxLength = max(maxLength, matrix[i][j])

        return maxLength * maxLength