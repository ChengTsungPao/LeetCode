class Solution:
    def searchMatrix(self, matrix, target):
        import numpy as np
        if(len(np.where(np.array(matrix)==target)[0])==0):
            return False
        else:
            return True