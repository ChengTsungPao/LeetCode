class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def divide_and_conquer(left, right, up, down):
            if left > right or up > down:
                return False

            row = up + (down - up) // 2
            col = bisect.bisect_right(matrix[row], target) - 1
            if matrix[row][col] == target:
                return True
            
            return divide_and_conquer(left, col, row + 1, down) or divide_and_conquer(col, right, up, row - 1)

        return divide_and_conquer(0, len(matrix[0]) - 1, 0, len(matrix) - 1)