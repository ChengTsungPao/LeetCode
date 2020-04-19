class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):   
                if(matrix[i][j]==0):
                    for k in range(len(matrix)):
                        if(matrix[k][j]!=0):
                            matrix[k][j]="ok"
                        else:
                            matrix[k][j]="no"
                    break                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]=="no"):
                    for k in range(len(matrix[0])):
                        matrix[i][k]="ok"
                    break
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]=="ok"):
                    matrix[i][j] = 0