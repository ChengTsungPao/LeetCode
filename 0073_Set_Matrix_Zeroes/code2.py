class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0])
        isZeroRow = isZeroCol = False
        
        # 先判斷第一列或第一行是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                isZeroRow = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                isZeroCol = True
                break
            
            
        # 將0出現在 "第幾列紀錄在第一行" 以及 "第幾行記錄在第一列"
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        
        # 將 "第一行出現0的位置整列改成0" 和 "第一列出現0的位置整行改成0"
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
                    
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        
        # 最後在處理第一列或第一行是否有0，是否要將第一行或第一列改成0
        if isZeroRow:
            for i in range(m):
                matrix[i][0] = 0
                
        if isZeroCol:
            for j in range(n):
                matrix[0][j] = 0