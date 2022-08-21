class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        def isValid(subarray):
            if len(subarray) == 2:
                return subarray[0] == subarray[1]
            elif len(subarray) == 3:
                return subarray[0] == subarray[1] == subarray[2] or (subarray[0] == subarray[1] - 1 and subarray[1] + 1 == subarray[2])
            else:
                return False
        
        n = len(nums)
        
        dp = [False] * (n + 1)
        dp[-1] = True
        
        for i in range(n - 1, -1, -1):
            if i + 2 <= n and dp[i + 2] and isValid(nums[i: i + 2]):
                dp[i] = True
            elif i + 3 <= n and dp[i + 3] and isValid(nums[i: i + 3]):
                dp[i] = True
                
        return dp[0]