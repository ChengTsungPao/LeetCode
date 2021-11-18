class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        dp[i][target] = 前i個總合為target的次數
        
        Init:
            cost = 數字總合
            score = 總合為target的所有可能
        
            dp[1,  nums[0]] = 1        
            dp[1, -nums[0]] = 1
        
        Method:
            dp[i][target] = dp[i - 1][target + nums[i]] + dp[i - 1][target - nums[i]]
        '''
        
        maxTarget = sum(nums)
        minTarget = -maxTarget
        
        dp = collections.defaultdict(int)
        
        dp[1,  nums[0]] += 1        
        dp[1, -nums[0]] += 1
            
        for i in range(2, len(nums) + 1):
            for target_ in range(minTarget, maxTarget + 1):
                dp[i, target_] = dp[i - 1, target_ + nums[i - 1]] + dp[i - 1, target_ - nums[i - 1]]
        
        return dp[len(nums), target]