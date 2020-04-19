class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = sum(matrix, [])
        index = bisect.bisect_left(mat,target)
        if(index>=len(mat) or mat[index]!=target):
            return False
        else:
            return True