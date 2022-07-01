class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        from sortedcontainers import SortedList
        
        def maxSubarrySmallerThanK(nums):
            bst = SortedList()
            max_, sum_ = -float("inf"), 0
            for num in nums:
                bst.add(sum_)
                sum_ += num
                index = bst.bisect_left(sum_ - k)
                if index < len(bst):
                    max_ = max(max_, sum_ - bst[index])
            return max_
        
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