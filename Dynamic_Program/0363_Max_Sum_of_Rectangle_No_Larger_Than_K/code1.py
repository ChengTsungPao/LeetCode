from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        # transpose
        if n > m:
            transpose_matrix = [[0] * m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    transpose_matrix[j][i] = matrix[i][j]
            return self.maxSumSubmatrix(transpose_matrix, k)
        
        # preSum
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
                
        def getMaxSumSubarray(arr):
            # Kadane Algorithm
            _sum = 0
            _max = -float("inf")
            for num in arr:
                _sum += num
                _max = max(_max, _sum)
                if _sum < 0:
                    _sum = 0
            if _max <= k:
                return _max
            
            # binary search tree
            bst = SortedList([0])
            _sum = 0
            _max = -float("inf")
            for num in arr:
                _sum += num
                idx = bst.bisect_left(_sum - k) # _sum - k <= target
                if idx < len(bst):
                    _max = max(_max, _sum - bst[idx])
                bst.add(_sum)
                
            return _max
            
        ans = -float("inf")
        for j1 in range(n):
            for j2 in range(j1, n):
                arr = [matrix[i][j2] if j1 == 0 else matrix[i][j2] - matrix[i][j1 - 1] for i in range(m)]
                ans = max(ans, getMaxSumSubarray(arr))
                
        return ans