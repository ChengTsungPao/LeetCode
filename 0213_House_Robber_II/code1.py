class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n <= 2:
            return max(nums)
        
        def simulation(i, j):
            length = j - i + 1
            if length <= 2:
                return max(nums[i: j + 1]) if length > 0 else 0
            
            dp = [0] * length
            dp[0] = nums[i]
            dp[1] = max(nums[i], nums[i + 1])
            for k in range(i + 2, j + 1):
                d = k - i
                dp[d] = max(nums[k] + dp[d - 2], dp[d - 1])
            return dp[-1]

        # consider first、consider last、no consider first and last
        return max(simulation(0, n - 2), simulation(1, n - 1))