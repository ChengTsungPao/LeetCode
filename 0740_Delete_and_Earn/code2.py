class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # dp[i] => 數字大小從 1 ~ i 之最大取法
        #       => 來源1: 有拿取與 i 相鄰之數字 dp[i - 1] <----- 拿取 i 後，需刪除 i - 1
        #       => 來源2: 沒拿取與 i 相鄰之數字 dp[i - 2] + i * nums[i]
        
        nums = collections.Counter(nums)
        length = max(nums.keys())

        dp = [0, 1 * nums[1]]        
        for i in range(2, length + 1):
            dp.append(max(dp[i - 1], dp[i - 2] + i * nums[i]))
        
        return dp[-1]
