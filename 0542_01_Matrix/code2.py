class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        height, width = len(mat), len(mat[0])
        
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    continue
                elif i - 1 >= 0 and j - 1 >= 0:
                    mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1)
                elif i - 1 >= 0:
                    mat[i][j] = mat[i - 1][j] + 1
                elif j - 1 >= 0:
                    mat[i][j] = mat[i][j - 1] + 1
                else:
                    mat[i][j] = float("inf")
                   
        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                elif i + 1 < height and j + 1 < width:
                    mat[i][j] = min(mat[i][j], mat[i + 1][j] + 1, mat[i][j + 1] + 1)
                elif i + 1 < height:
                    mat[i][j] = min(mat[i][j], mat[i + 1][j] + 1)
                elif j + 1 < width:
                    mat[i][j] = min(mat[i][j], mat[i][j + 1] + 1)
     
        return mat
