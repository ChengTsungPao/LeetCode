class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        direction = [
            ( 0,  1),
            ( 1,  0),
            ( 0, -1),
            (-1,  0),
        ]
        
        def nextIndex(i, j, index):
            di, dj = direction[index]
            newI, newJ = i + di, j + dj
            if not (0 <= newI < n and 0 <= newJ < n) or matrix[newI][newJ] > 0:
                return nextIndex(i, j, (index + 1) % 4)
            return newI, newJ, index
        
        matrix = [[0] * n for _ in range(n)]
        
        i = j = index = 0
        for num in range(1, n * n):
            matrix[i][j] = num
            i, j, index = nextIndex(i, j, index)
        matrix[i][j] = n * n
        
        return matrix