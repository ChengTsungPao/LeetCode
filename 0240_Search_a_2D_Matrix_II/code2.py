class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def BinarySearch(left, right, index, direct):            
            if direct:
                while left < right:
                    mid = (left + right) // 2
                    if matrix[index][mid] == target:
                        return mid
                    elif matrix[index][mid] < target:
                        left = mid + 1
                    else:
                        right = mid
            else:
                while left < right:
                    mid = (left + right) // 2
                    if matrix[mid][index] == target:
                        return mid
                    elif matrix[mid][index] < target:
                        left = mid + 1
                    else:
                        right = mid
   
            return (left + right) // 2
        
        def divide_and_conquer(left, up, right, down):
            if left > right or up > down or left < 0 or up < 0 or right >= len(matrix[0]) or down >= len(matrix):
                return False
            
            col = BinarySearch(left, right, up, True)
            row = BinarySearch(up, down, col, False)
            
            if matrix[row][col] == target or matrix[up][col] == target:
                return True
            
            return divide_and_conquer(left, row, col - 1, down) or divide_and_conquer(col + 1, up + 1, right, row)
        
        return divide_and_conquer(0, 0, len(matrix[0]) - 1, len(matrix) - 1)