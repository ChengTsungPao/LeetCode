class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # 利用01背包問題的方法，將物品價值和重量都設為nums，找尋當背包重量為 sum(nums) // 2 是否能裝到價值為 sum(nums) // 2
        
        weight = sum(nums)
        if weight % 2 == 1:
            return False
        weight //= 2
        
        dp = [[0] * (weight + 1) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for w in range(1, weight + 1):
                if w - nums[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - nums[i - 1]] + nums[i - 1])
           
        return dp[-1][-1] == weight
