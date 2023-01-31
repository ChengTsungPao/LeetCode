class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m // 2):
            for j in range(n):
                matrix[i][j], matrix[~i][j] = matrix[~i][j], matrix[i][j]
        
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

