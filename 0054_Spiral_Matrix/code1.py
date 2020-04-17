class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if(matrix==[]): return []
        ans = []
        i = 0
        j = 0
        flag = True
        while flag:
            flag = False
            while 1==1:
                if(j < len(matrix[0]) and matrix[i][j]!="#"):
                    flag = True
                    ans.append(matrix[i][j])
                    matrix[i][j] = "#"
                    j += 1
                else:
                    i += 1
                    j -= 1
                    break
                    
            while 1==1:
                if(i < len(matrix) and matrix[i][j]!="#"):
                    flag = True
                    ans.append(matrix[i][j])
                    matrix[i][j] = "#"
                    i += 1
                else:
                    i -= 1
                    j -= 1
                    break 
                    
            while 1==1:
                if(j >= 0 and matrix[i][j]!="#"):
                    flag = True
                    ans.append(matrix[i][j])
                    matrix[i][j] = "#"
                    j -= 1
                else:
                    i -= 1
                    j += 1
                    break
                    
            while 1==1:
                if(i >= 0 and matrix[i][j]!="#"):
                    flag = True
                    ans.append(matrix[i][j])
                    matrix[i][j] = "#"
                    i -= 1
                else:
                    i += 1
                    j += 1
                    break
                    
        return ans