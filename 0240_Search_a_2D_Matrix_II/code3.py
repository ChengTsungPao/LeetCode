class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_range, col_range = [0, len(matrix[0]) - 1], [0, len(matrix) - 1]
        
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
        
        while row_range[0] <= row_range[1] or col_range[0] <= col_range[1]:
            
            if col_range[0] < len(matrix):
                row_index = BinarySearch(row_range[0], row_range[1], col_range[0], True)
                if row_index < len(matrix[0]) and matrix[col_range[0]][row_index] == target:
                    return True
                
            if row_range[0] < len(matrix[0]):
                col_index = BinarySearch(col_range[0], col_range[1], row_range[0], False)
                if col_index < len(matrix) and matrix[col_index][row_range[0]] == target:
                    return True

            row_range = [row_range[0] + 1, row_index]
            col_range = [col_range[0] + 1, col_index]
                
        return False
