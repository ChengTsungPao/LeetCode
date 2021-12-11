class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix != []:
            length = min(len(matrix), len(matrix[0]))
            matrix[0][0] = (matrix[0][0] == "1") * 1
            for i in range(1, len(matrix)):
                matrix[i][0] = matrix[i - 1][0] + (matrix[i][0] == "1") * 1
            for i in range(1, len(matrix[0])):
                matrix[0][i] = matrix[0][i - 1] + (matrix[0][i] == "1") * 1
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = (matrix[i][j] == "1") + \
                                   int(matrix[i - 1][j]) + \
                                   int(matrix[i][j - 1]) - \
                                    matrix[i - 1][j - 1]
            for i in range(length):
                for j in range(abs(len(matrix) - length) + i + 1):
                    for k in range(abs(len(matrix[0]) - length) + i + 1):
                        if (length - i) ** 2 == \
                            matrix[length - i + j - 1][length - i + k - 1] - \
                            matrix[j - 1][length - i + k - 1] * (j != 0) - \
                            matrix[length - i + j - 1][k - 1] * (k != 0) + \
                            matrix[j -1][k - 1] * (j != 0) * (k != 0):
                            return (length - i) ** 2
        return 0