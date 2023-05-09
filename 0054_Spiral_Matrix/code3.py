class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def nextPosition(i, j, d):
            di, dj = direction[d]
            i_, j_ = i + di, j + dj
            if not (0 <= i_ < m) or not (0 <= j_ < n) or matrix[i_][j_] == "#":
                return nextPosition(i, j, (d + 1) % 4)
            return i_, j_, d
        
        ans = []
        i = j = d = 0
        for _ in range(m * n - 1):
            ans.append(matrix[i][j])
            matrix[i][j] = "#"
            i, j, d = nextPosition(i, j, d)
        ans.append(matrix[i][j])
            
        return ans