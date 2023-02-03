class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        # cal all costs
        costs = {}
        for i in range(n):
            cost = k
            countNum = {}
            for j in range(i, n):
                if nums[j] not in countNum:
                    countNum[nums[j]] = 0
                countNum[nums[j]] += 1
                if countNum[nums[j]] != 1:
                    cost += 2 if countNum[nums[j]] == 2 else 1
                costs[i, j] = cost
                
        # dp
        dp = [float("inf")] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i] = min(dp[i], costs[i, j] + dp[j + 1])
                
        return dp[0]