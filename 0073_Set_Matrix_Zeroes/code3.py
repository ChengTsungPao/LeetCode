class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # 方法: 用其中一個零所在的行列來mark
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        # 將存在0的行列標記在"第markI列"和"第markJ行"
        markI = markJ = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if markI < 0:
                        markI, markJ = i, j
                    else:
                        matrix[i][markJ] = 0
                        matrix[markI][j] = 0
        if markI < 0:
            return
        
        
        # 處理 第markI列 和 第markJ行 以外的行列
        for i in range(m):
            if matrix[i][markJ] == 0 and i != markI:
                for j in range(n):
                    matrix[i][j] = 0
                    
        for j in range(n):
            if matrix[markI][j] == 0 and j != markJ:
                for i in range(m):
                    matrix[i][j] = 0
                    
                    
        # 處理 第markI列 和 第markJ行
        for i in range(m):
            matrix[i][markJ] = 0
            
        for j in range(n):
            matrix[markI][j] = 0 
