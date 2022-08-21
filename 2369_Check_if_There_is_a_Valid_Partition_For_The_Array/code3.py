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
        
        dp = [False, isValid(nums[:2]), isValid(nums[:3]), False]
        
        for i in range(3, n):
            dp[i % 4] = False
            if isValid(nums[i - 1: i + 1]) and dp[(i - 2) % 4]:
                dp[i % 4] = True
            elif isValid(nums[i - 2: i + 1]) and dp[(i - 3) % 4]:
                dp[i % 4] = True
            else:
                dp[i % 4] = False
                
        return dp[(n - 1) % 4]