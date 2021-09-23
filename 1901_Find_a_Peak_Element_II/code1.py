class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        # 往高處爬總會爬到高點，若為row pick就去找col pick，反之亦然
        
        def findRowPeakElement(row):
            left = 0
            right = len(mat[row]) - 1
            while left != right:
                mid = (left + right) // 2
                if mat[row][mid] > mat[row][mid + 1]:
                    right = mid
                else:
                    left = mid + 1
            return row, left
        
        def findColPeakElement(col):
            left = 0
            right = len(mat) - 1
            while left != right:
                mid = (left + right) // 2
                if mat[mid][col] > mat[mid + 1][col]:
                    right = mid
                else:
                    left = mid + 1
            return left, col
        
        def isPick(row, col):
            for x, y in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if not (0 <= x < len(mat)) or not (0 <= y < len(mat[0])):
                    continue
                if mat[row][col] < mat[x][y]:
                    return False
            return True
        
        row, col = 0, 0
        while True:
            row, col = findRowPeakElement(row)
            if isPick(row, col):
                return [row, col]
            row, col = findColPeakElement(col)
            if isPick(row, col):
                return [row, col]  