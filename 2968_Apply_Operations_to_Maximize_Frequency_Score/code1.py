class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort()
        preSum = [nums[0]] * n
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i]
            
        def getRangeSum(i, j):
            return preSum[j] - preSum[i - 1] if i > 0 else preSum[j]
        
        def condition(frequency):
            for i in range(n - frequency + 1):
                j = i + frequency - 1
                m = (i + j) // 2
                mid = nums[m]
                leftAbsDiff = mid * (m - i + 1) - getRangeSum(i, m)
                rightAbsDiff = getRangeSum(m, j) - mid * (j - m + 1)
                diff = leftAbsDiff + rightAbsDiff
                if diff <= k:
                    return True
            return False
        
        ans = 1
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if condition(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans