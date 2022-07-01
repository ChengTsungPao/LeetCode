class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        from sortedcontainers import SortedList
        
        def transpose(matrix):
            m = len(matrix)
            n = len(matrix[0])
            transposeMatrix = [[0] * m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    transposeMatrix[j][i] = matrix[i][j]
            return matrix

        def maxSubarrySmallerThanK(nums):
            
            # kadane's algorithm
            max_, sum_ = -float("inf"), 0
            for num in nums:
                sum_ += num
                max_ = max(max_, sum_)
                if sum_ < 0:
                    sum_ = 0
            if max_ <= k:
                return max_
            
            # preSum + bst
            bst = SortedList()
            max_, sum_ = -float("inf"), 0
            for num in nums:
                bst.add(sum_)
                sum_ += num
                index = bst.bisect_left(sum_ - k)
                if index < len(bst):
                    max_ = max(max_, sum_ - bst[index])
            return max_
        
        if len(matrix) > len(matrix[0]):
            matrix = transpose(matrix)
        
        m = len(matrix)
        n = len(matrix[0])

        colPreSum = [[0] * n for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(n):
                colPreSum[r][c] = matrix[r - 1][c] + colPreSum[r - 1][c]
                
        ans = -float("inf")
        for r1 in range(1, m + 1):
            for r2 in range(r1):
                nums = [colPreSum[r1][c] - colPreSum[r2][c] for c in range(n)]
                ans = max(ans, maxSubarrySmallerThanK(nums))
                
        return ans