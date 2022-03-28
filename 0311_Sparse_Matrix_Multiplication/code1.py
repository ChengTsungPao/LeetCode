class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m = len(mat1)
        p = len(mat1[0])
        n = len(mat2[0])
        
        mat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    mat[i][j] += mat1[i][k] * mat2[k][j]
                    
        return mat