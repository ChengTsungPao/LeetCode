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
        
        dp = collections.deque([True])
        
        for i in range(n - 1, -1, -1):
            if isValid(nums[i: i + 2]) and dp[2 - 1]:
                dp.appendleft(True)
            elif isValid(nums[i: i + 3]) and dp[3 - 1]:
                dp.appendleft(True)
            else:
                dp.appendleft(False)
            
            if len(dp) > 3: dp.pop()
                
        return dp[0]