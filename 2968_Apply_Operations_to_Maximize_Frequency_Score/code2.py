class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort()
        preSum = [nums[0]] * n
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i]
            
        def getRangeSum(i, j):
            return preSum[j] - preSum[i - 1] if i > 0 else preSum[j]
        
        def isValid(i, j):
            m = (i + j) // 2
            mid = nums[m]
            leftAbsDiff = mid * (m - i + 1) - getRangeSum(i, m)
            rightAbsDiff = getRangeSum(m, j) - mid * (j - m + 1)
            diff = leftAbsDiff + rightAbsDiff
            return diff <= k
        
        ans = i = 0
        for j in range(n):
            while not isValid(i, j):
                i += 1
            ans = max(ans, (j - i + 1))
                
        return ans