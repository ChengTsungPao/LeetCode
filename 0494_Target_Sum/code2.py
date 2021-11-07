class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        dp[ nums[0]] = dp.get( nums[0], 0) + 1
        dp[-nums[0]] = dp.get(-nums[0], 0) + 1
        
        for index in range(1, len(nums)):
            temp = {}
            for sum_ in dp.keys():
                newSum = sum_ + nums[index]
                temp[ newSum] = temp.get( newSum, 0) + dp[sum_]
                temp[-newSum] = temp.get(-newSum, 0) + dp[sum_]
            dp = temp.copy()
            
        return dp.get(target, 0)