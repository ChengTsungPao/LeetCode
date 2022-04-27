class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        n = len(nums)
        total = sum(nums)
        target = total - x
        
        if target == 0:
            return n
        
        maxLength = 0
        s = 0
        dp = {0: -1}
        for i in range(n):
            s += nums[i]
            if s - target in dp:
                maxLength = max(maxLength, i - dp[s - target])
            dp[s] = i

        return n - maxLength if maxLength > 0 else -1