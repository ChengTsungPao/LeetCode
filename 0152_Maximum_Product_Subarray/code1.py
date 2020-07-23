class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        def maxProfit(prices):
            ans = -float("inf")
            min_p = float("inf")
            min_n = -float("inf")
            for i in range(len(prices) - 1):
                if prices[i] > 0 and prices[i] < min_p:
                    min_p = prices[i]
                elif prices[i] < 0 and prices[i] > min_n:
                    min_n = prices[i]
                if min_p != float("inf") and prices[i + 1] > 0 and prices[i + 1] // min_p > ans:
                    ans = prices[i + 1] // min_p
                elif min_n != -float("inf") and prices[i + 1] < 0 and prices[i + 1] // min_n > ans:
                    ans = prices[i + 1] // min_n
            return ans        
        
        data = [[1]]
        for n in nums:
            if n != 0:
                data[-1] += [data[-1][-1] * n]
            else:
                data += [[1]]
        
        ans = -float("inf")
        for arr in data:
            ans = max(ans, maxProfit(arr))
        
        if ans < 0 and len(data) != 1:
            return 0
        else:
            return ans