class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def getNextPosition(i, j, d):
            di, dj = direction[d]
            i_, j_ = i + di, j + dj
            if not (0 <= i_ < m and 0 <= j_ < n) or matrix[i_][j_] == "":
                return getNextPosition(i, j, (d + 1) % 4)
            return i_, j_, d
        
        i = j = d = 0
        ans = []
        for k in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = ""
            if len(ans) < m * n :
                i, j, d = getNextPosition(i, j, d)
            
        return ans
    