class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for j in range(len(matrix) - 1, -1, -1):
            for i in range(len(matrix) - 1, -1, -1):                
                matrix[j].append(matrix[i].pop(j))
