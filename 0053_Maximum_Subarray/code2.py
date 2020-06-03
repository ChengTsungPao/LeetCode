class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def maxProfit(prices):
            ans = -float("inf")
            min_ = float("inf")
            for i in range(len(prices) - 1):
                if prices[i] < min_:
                    min_ = prices[i]
                if prices[i + 1] - min_ > ans:
                    ans = prices[i + 1] - min_
            return ans
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]  
        nums.insert(0, 0)
        return maxProfit(nums)