class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def move(i, j, index):
            if index == 0:
                return i, j + 1
            elif index == 1:
                return i + 1, j
            elif index == 2:
                return i, j - 1
            else:
                return i - 1, j
        
        ans = [matrix[0][0]]
        matrix[0][0] = "#"
        count = 1
        index = 0
        i, j = 0, 0
        
        while count < len(matrix) * len(matrix[0]):
            nextI, nextJ = move(i, j, index)
            if (not (0 <= nextI < len(matrix) and 0 <= nextJ < len(matrix[0]))) or matrix[nextI][nextJ] == "#":
                index = (index + 1) % 4
                nextI, nextJ = move(i, j, index)
            
            ans.append(matrix[nextI][nextJ])
            matrix[nextI][nextJ] = "#"
            i, j = nextI, nextJ
            count += 1
            
        return ans