class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # 轉置
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 左右對調
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
